"""Generate and cache private, standalone reports."""
import hashlib
import html
import json
import os
import tempfile
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path
from string import Template
from ...core.record.query import read_records

TEMPLATES = Path(__file__).resolve().parents[2] / 'resource' / 'report_templates'


def safe(value):
    return html.escape(str(value), quote=True)


def number(value):
    return value if isinstance(value, (int, float)) and not isinstance(value, bool) and 0 <= value < 1e9 else None


def chart(days, data, fields, colors):
    width, height, top, bottom = 920, 220, 15, 35
    maximum = max((sum(number(data.get(day, {}).get(f)) or 0 for f in fields) for day in days), default=0) or 1
    bar_width = min(24, 840 / max(len(days), 1) * .7)
    parts = [f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="每日趋势图">']
    for i, day in enumerate(days):
        row = data.get(day)
        x = 55 + (i + .5) * 840 / max(len(days), 1)
        y = height - bottom
        if row is None or all(number(row.get(f)) is None for f in fields):
            parts.append(f'<text x="{x:.1f}" y="{y}" fill="#9aa89d" text-anchor="middle">·</text>')
        else:
            for field, color in zip(fields, colors):
                value = number(row.get(field)) or 0
                h = value / maximum * (height - top - bottom)
                y -= h
                parts.append(f'<rect x="{x-bar_width/2:.2f}" y="{y:.2f}" width="{bar_width:.2f}" height="{h:.2f}" fill="{color}"><title>{safe(day)}: {value:g}</title></rect>')
        if len(days) <= 14 or i in (0, len(days)-1) or (len(days) > 14 and i % max(1, len(days)//6) == 0):
            parts.append(f'<text x="{x:.1f}" y="{height-8}" font-size="10" fill="#607469" text-anchor="middle">{safe(day[5:])}</text>')
    parts.append(f'<text x="0" y="22" font-size="11" fill="#607469">{maximum:g}</text></svg>')
    return ''.join(parts)


def render(rows, start, end, template):
    begin, finish = date.fromisoformat(start), date.fromisoformat(end)
    days = [(begin + timedelta(days=i)).isoformat() for i in range((finish-begin).days+1)]
    activities = {row['data'].get('day'): row['data'] for row in rows if row['kind'] == 'daily_activity' and row['data'].get('day') in days}
    workouts = [r['data'] for r in rows if r['kind'] == 'workout']
    steps = [number(row.get('steps')) for row in activities.values()]
    steps = [x for x in steps if x is not None]
    avg = f'{sum(steps)/len(steps):,.0f}' if steps else '暂无数据'
    cards = ''.join(f'<div class="card"><span class="muted">{label}</span><strong>{value}</strong></div>' for label,value in [('活动日报覆盖', f'{len(activities)} / {len(days)} 天'),('平均每日步数',avg),('训练记录',f'{len(workouts)} 次')])
    converted = {day:{'medium':(number(row.get('medium_activity_time')) or 0)/60 if number(row.get('medium_activity_time')) is not None else None,'high':(number(row.get('high_activity_time')) or 0)/60 if number(row.get('high_activity_time')) is not None else None} for day,row in activities.items()}
    weeks={}
    for day in days:
        dt=date.fromisoformat(day); monday=dt-timedelta(days=dt.weekday()); weeks.setdefault(monday,[]).append(day)
    week_rows=[]
    for monday, members in sorted(weeks.items()):
        vals=[converted[d] for d in members if d in converted]
        med=sum(v['medium'] or 0 for v in vals); high=sum(v['high'] or 0 for v in vals)
        complete=len(members)==7 and len(vals)==7 and all(v['medium'] is not None and v['high'] is not None for v in vals)
        week_rows.append(f'<tr><td>{monday}</td><td>{len(vals)}/7</td><td>{med:.1f}</td><td>{high:.1f}</td><td>{"完整" if complete else "不完整 / 未知"}</td></tr>')
    weeks_html='<table><thead><tr><th>周起始</th><th>覆盖天数</th><th>中等强度分钟</th><th>高强度分钟</th><th>覆盖状态</th></tr></thead><tbody>'+''.join(week_rows)+'</tbody></table>'
    counts=Counter(); valid=0.; invalid=0; workout_rows=[]
    for item in workouts:
        label=str(item.get('activity') or '未分类');counts[label]+=1
        try:
            a=datetime.fromisoformat(item['start_datetime'].replace('Z','+00:00')); b=datetime.fromisoformat(item['end_datetime'].replace('Z','+00:00'))
            if (a.tzinfo is None) != (b.tzinfo is None) or b <= a: raise ValueError
            mins=(b-a).total_seconds()/60; valid+=mins; duration=f'{mins:.1f} 分钟'
        except (KeyError,TypeError,ValueError,OverflowError): invalid+=1;duration='未知'
        workout_rows.append(f'<tr><td>{safe(item.get("day", "未知"))}</td><td>{safe(label)}</td><td>{duration}</td></tr>')
    distribution='、'.join(f'{safe(k)} {v} 次' for k,v in counts.most_common()) or '暂无训练记录'
    workout_html=f'<p class="muted">有效时长合计 {valid:.1f} 分钟；{invalid} 条时长未知。类型：{distribution}</p><table><thead><tr><th>日期</th><th>类型</th><th>时长</th></tr></thead><tbody>{"".join(workout_rows)}</tbody></table>'
    return Template(template).substitute(period=f'{safe(start)} — {safe(end)}', cards=cards, steps_chart=chart(days,activities,['steps'],['#5b9d75']), activity_chart=chart(days,converted,['medium','high'],['#5b9d75','#bd8c4c']),weeks=weeks_html,workouts=workout_html)


def generate_report(root, account_id, report_type, start, end, force=False):
    root=Path(root)
    if report_type != 'activity-trend': raise ValueError('Unknown report type')
    first,last=date.fromisoformat(start),date.fromisoformat(end)
    if first > last: raise ValueError('Start date must not be after end date')
    params={'account_id':account_id,'type':report_type,'start':first.isoformat(),'end':last.isoformat()}
    digest=hashlib.sha256(json.dumps(params,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    namehash=hashlib.sha256(report_type.encode()).hexdigest()
    directory=root.parent/'reports'; directory.mkdir(parents=True,exist_ok=True,mode=0o700); os.chmod(directory,0o700)
    target=directory/f'{digest}-{namehash}.html'
    if target.is_file() and not force: return {'path':str(target),'cached':True}
    template=(TEMPLATES / (report_type+'.html')).read_text(encoding='utf-8')
    rows=read_records(root,account_id,kinds=['daily_activity','workout'],start=start,end=end,limit=None)
    content=render(rows,start,end,template)
    fd,tmp=tempfile.mkstemp(dir=directory,prefix='.report-',suffix='.tmp')
    try:
        with os.fdopen(fd,'w',encoding='utf-8') as out: out.write(content)
        os.replace(tmp,target)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)
    return {'path':str(target),'cached':False}
