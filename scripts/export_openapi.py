#!/usr/bin/env python3
"""Export an OpenAPI JSON document as navigable Markdown files."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
METHODS = {'get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'trace'}


def block(value):
    return '```json\n' + json.dumps(value, ensure_ascii=False, indent=2) + '\n```\n'


def export(spec, output):
    output.mkdir(parents=True, exist_ok=True)
    info = spec.get('info', {})
    overview = ['# ' + info.get('title', 'OpenAPI'), '', info.get('description', ''), '']
    metadata = {k: v for k, v in spec.items() if k not in ('paths', 'components')}
    overview += ['## 完整元数据', '', block(metadata)]
    operations = ['# API 路径与操作', '', '以下 JSON 保留原始字段；`$ref` 指向组件文档中的定义。', '']
    for path, item in spec.get('paths', {}).items():
        operations += [f'## `{path}`', '']
        common = {k: v for k, v in item.items() if k.lower() not in METHODS}
        if common:
            operations += ['### 路径级配置', '', block(common)]
        for method, operation in item.items():
            if method.lower() in METHODS:
                operations += [f'### {method.upper()} — {operation.get("summary", path)}', '', block(operation)]
    components = ['# 可复用组件', '']
    for category, entries in spec.get('components', {}).items():
        components += [f'## {category}', '']
        for name, value in entries.items():
            components += [f'### `{name}`', '', block(value)]
    files = {
        'README.md': '# Oura API 文档\n\n由 `docs/openapi-1.43.json` 生成，请勿直接编辑。\n\n- [概览与元数据](overview.md)\n- [路径与操作](operations.md)\n- [可复用组件](components.md)\n\n在仓库根目录运行 `python3 scripts/export_openapi.py` 更新。\n',
        'overview.md': '\n'.join(overview),
        'operations.md': '\n'.join(operations),
        'components.md': '\n'.join(components),
    }
    for name, content in files.items():
        (output / name).write_text(content.rstrip() + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=ROOT / 'docs' / 'openapi-1.43.json')
    parser.add_argument('--output', type=Path, default=ROOT / 'docs' / 'oura-api')
    args = parser.parse_args()
    with args.input.open(encoding='utf-8') as source:
        export(json.load(source), args.output)


if __name__ == '__main__':
    main()
