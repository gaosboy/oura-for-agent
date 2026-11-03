import json
import tempfile
import unittest
from pathlib import Path

from scripts.export_openapi import export


class ExportTests(unittest.TestCase):
    def test_exports_operations_components_and_metadata(self):
        spec = {'openapi': '3.1.0', 'info': {'title': 'Example', 'version': '1'},
                'paths': {'/items': {'get': {'tags': ['Items'], 'summary': 'List items', 'responses': {'200': {'description': 'OK'}}}}},
                'components': {'schemas': {'Item': {'type': 'object'}}}}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            export(spec, root)
            self.assertIn('List items', (root / 'operations.md').read_text())
            self.assertIn('"description": "OK"', (root / 'operations.md').read_text())
            self.assertIn('`Item`', (root / 'components.md').read_text())
            self.assertIn('Example', (root / 'overview.md').read_text())
            self.assertTrue((root / 'README.md').exists())


if __name__ == '__main__':
    unittest.main()
