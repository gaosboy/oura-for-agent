import tempfile
import unittest
from pathlib import Path
from oura_app.core.account.setup import initialize
from oura_app.core.account.login import save_authorization
from oura_app.core.record.sync import sync_range, sync_incremental
from oura_app.core.record.query import read_records

class RecordSyncTests(unittest.TestCase):
 def test_remote_update_pagination_and_query(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory); initialize(root)
   account=save_authorization(root,'user',{'access_token':'x'},lambda x:x.encode())
   def remote(kind,start,end):
    return iter([{'id':'a','day':'2026-01-02','score':10}])
   sync_range(root,account,'x','2026-01-01','2026-01-03',['daily_sleep'],remote)
   def updated(kind,start,end):
    return iter([{'id':'a','day':'2026-01-02','score':20},{'id':'b','day':'2026-01-03','score':30}])
   sync_range(root,account,'x','2026-01-01','2026-01-03',['daily_sleep'],updated)
   rows=read_records(root,account,kinds=['daily_sleep'],start='2026-01-02',end='2026-01-02')
   self.assertEqual(len(rows),1); self.assertEqual(rows[0]['data']['score'],20)
   result=sync_incremental(root,account,'x','2026-01-04',kinds=['daily_sleep'],fetch=updated)
   self.assertEqual(result['status'],'succeeded')

 def test_failure_rolls_back_and_incremental_requires_baseline(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory); initialize(root)
   account=save_authorization(root,'user',{'access_token':'x'},lambda x:x.encode())
   def broken(kind,start,end):
    yield {'id':'a','day':'2026-01-02'}
    raise RuntimeError('failed')
   result=sync_range(root,account,'x','2026-01-01','2026-01-03',['daily_sleep'],broken)
   self.assertEqual(result['status'],'failed')
   self.assertEqual(read_records(root,account,kinds=['daily_sleep']),[])
   with self.assertRaises(ValueError): sync_incremental(root,account,'x','2026-01-04',['daily_sleep'],broken)

 def test_sample_remote_correction_replaces_previous_values(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory); initialize(root)
   account=save_authorization(root,'user',{'access_token':'x'},lambda x:x.encode())
   def remote(bpm): return lambda kind,start,end: iter([{'timestamp_unix':1767312000000,'source':'awake','bpm':bpm}])
   sync_range(root,account,'x','2026-01-01','2026-01-03',['heartrate'],remote(50))
   sync_range(root,account,'x','2026-01-01','2026-01-03',['heartrate'],remote(60))
   rows=read_records(root,account,['heartrate'])
   self.assertEqual([r['data']['bpm'] for r in rows],[60])

 def test_pagination_and_token_cycles(self):
  from unittest.mock import patch
  from oura_app.link.oura_v2.api import collection
  pages=[{'data':[{'id':'a'}],'next_token':'next'}, {'data':[{'id':'b'}],'next_token':None}]
  with patch('oura_app.link.oura_v2.api.request_json',side_effect=pages):
   self.assertEqual([x['id'] for x in collection('sleep','2026-01-01','2026-01-02','x')], ['a','b'])
  with patch('oura_app.link.oura_v2.api.request_json',return_value={'data':[],'next_token':'same'}):
   with self.assertRaises(ValueError): list(collection('sleep','2026-01-01','2026-01-02','x'))

 def test_time_series_requests_are_split_into_21_day_windows(self):
  from unittest.mock import patch
  from urllib.parse import urlsplit, parse_qs
  from oura_app.link.oura_v2.api import collection
  urls=[]
  def fake(url, token):
   urls.append(url); return {'data': [], 'next_token':None}
  with patch('oura_app.link.oura_v2.api.request_json', side_effect=fake):
   list(collection('heartrate','2026-10-01','2026-10-31','x','datetime'))
  self.assertEqual(len(urls),2)
  first,second=[parse_qs(urlsplit(url).query) for url in urls]
  self.assertEqual(first['end_datetime'][0], '2026-10-22T00:00:00Z')
  self.assertEqual(first['end_datetime'][0], second['start_datetime'][0])
  self.assertEqual(second['end_datetime'][0], '2026-11-01T00:00:00Z')

 def test_date_windows_are_inclusive_and_sequential(self):
  from unittest.mock import patch
  from urllib.parse import urlsplit, parse_qs
  from oura_app.link.oura_v2.api import collection
  urls=[]
  def fake(url, token):
   urls.append(parse_qs(urlsplit(url).query)); return {'data': [], 'next_token':None}
  with patch('oura_app.link.oura_v2.api.request_json', side_effect=fake):
   list(collection('daily_sleep','2026-01-01','2026-02-12','x','date'))
  self.assertEqual([(x['start_date'][0],x['end_date'][0]) for x in urls], [('2026-01-01','2026-01-21'),('2026-01-22','2026-02-11'),('2026-02-12','2026-02-12')])

 def test_sample_iso_timestamp_without_unix_is_supported(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory); initialize(root)
   account=save_authorization(root,'user',{'access_token':'x'},lambda x:x.encode())
   def remote(kind,start,end):
    return iter([{'timestamp':'2026-10-01T02:30:00+02:00','bpm':60,'source':'awake'}])
   result=sync_range(root,account,'x','2026-10-01','2026-10-01',['heartrate'],remote)
   self.assertEqual(result['status'],'succeeded')
   self.assertEqual(len(read_records(root,account,['heartrate'],start='2026-10-01',end='2026-10-01')),1)

 def test_debug_logging_window_and_page_omits_token(self):
  from unittest.mock import patch
  from oura_app.link.oura_v2.api import collection
  with patch('oura_app.link.oura_v2.api.request_json',return_value={'data':[],'next_token':None}):
   with self.assertLogs('oura_app.link.oura_v2.api', level='DEBUG') as logs:
    list(collection('heartrate','2026-10-01','2026-10-22','very-secret','datetime'))
  self.assertGreaterEqual(len(logs.output),4)
  self.assertNotIn('very-secret', ' '.join(logs.output))
