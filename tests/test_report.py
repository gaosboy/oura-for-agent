import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from oura_app.action.operations.report import generate_report

class ReportTests(unittest.TestCase):
 def test_cache_force_and_account_isolation(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d)/'data'; rows=[{'kind':'daily_activity','data':{'day':'2026-01-01','steps':100,'medium_activity_time':600,'high_activity_time':0}}]
   with patch('oura_app.action.operations.report.read_records',return_value=rows) as reader:
    a=generate_report(root,'account-a','activity-trend','2026-01-01','2026-01-07')
    first=Path(a['path']).read_text(); self.assertIn('100',first)
    rows[0]['data']['steps']=200
    b=generate_report(root,'account-a','activity-trend','2026-01-01','2026-01-07')
    self.assertTrue(b['cached']); self.assertEqual(reader.call_count,1)
    c=generate_report(root,'account-a','activity-trend','2026-01-01','2026-01-07',force=True)
    self.assertFalse(c['cached']); self.assertIn('200',Path(c['path']).read_text())
    other=generate_report(root,'account-b','activity-trend','2026-01-01','2026-01-07')
    self.assertNotEqual(a['path'],other['path'])

 def test_empty_and_html_escaping(self):
  with tempfile.TemporaryDirectory() as d:
   rows=[{'kind':'workout','data':{'day':'2026-01-02','activity':'<script>alert(1)</script>','start_datetime':'bad','end_datetime':'bad'}}]
   with patch('oura_app.action.operations.report.read_records',return_value=rows):
    report=generate_report(Path(d)/'data','x','activity-trend','2026-01-01','2026-01-07')
   text=Path(report['path']).read_text()
   self.assertNotIn('<script>alert(1)</script>',text); self.assertIn('&lt;script&gt;',text)
   self.assertIn('覆盖',text)

 def test_force_failure_preserves_report(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d)/'data'
   with patch('oura_app.action.operations.report.read_records',return_value=[]):
    report=generate_report(root,'a','activity-trend','2026-01-01','2026-01-02')
   path=Path(report['path']); before=path.read_bytes()
   with patch('oura_app.action.operations.report.read_records',side_effect=RuntimeError('failure')):
    with self.assertRaises(RuntimeError): generate_report(root,'a','activity-trend','2026-01-01','2026-01-02',True)
   self.assertEqual(path.read_bytes(),before)

 def test_reads_all_records_and_invalid_range(self):
  with tempfile.TemporaryDirectory() as d:
   rows=[{'kind':'workout','data':{'day':'2026-01-01','activity':'walk','start_datetime':'2026-01-01T00:00:00Z','end_datetime':'2026-01-01T00:10:00Z'}} for _ in range(1001)]
   with patch('oura_app.action.operations.report.read_records',return_value=rows) as reader:
    report=generate_report(Path(d)/'data','a','activity-trend','2026-01-01','2026-01-01')
    self.assertIsNone(reader.call_args.kwargs['limit'])
    self.assertIn('1001 次',Path(report['path']).read_text())
   with self.assertRaises(ValueError): generate_report(Path(d)/'data','a','activity-trend','2026-02-01','2026-01-01')

 def test_unlimited_query_reads_more_than_1000_rows(self):
  from oura_app.core.account.setup import initialize
  from oura_app.core.account.login import save_authorization
  from oura_app.core.record.access import record_path
  from oura_app.common.storage import transaction
  from oura_app.core.record.query import read_records
  with tempfile.TemporaryDirectory() as d:
   root=Path(d); initialize(root)
   account=save_authorization(root,'fake',{'access_token':'fake'},lambda s:s.encode())
   with transaction(record_path(root, account)) as db:
    db.executemany('INSERT INTO records(kind,source_id,day,payload_json,first_seen_at,last_seen_at) VALUES (?,?,?,?,?,?)', [('workout',str(i),'2026-01-01','{}','t','t') for i in range(1001)])
   self.assertEqual(len(read_records(root,account,['workout'],start='2026-01-01',end='2026-01-01',limit=None)),1001)

 def test_report_directory_is_sibling_of_data_directory(self):
  with tempfile.TemporaryDirectory() as d:
   data = Path(d) / 'data'
   with patch('oura_app.action.operations.report.read_records', return_value=[]):
    result=generate_report(data,'a','activity-trend','2026-01-01','2026-01-02')
   self.assertEqual(Path(result['path']).parent, Path(d) / 'reports')
