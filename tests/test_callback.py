import threading
import unittest
import urllib.error
import urllib.request
from core.core.account.callback import CallbackServer

class CallbackTests(unittest.TestCase):
    def test_idle_browser_connection_does_not_block_callback_or_shutdown(self):
        import socket
        with CallbackServer('http://localhost:0/callback', 'valid') as server:
            idle = socket.create_connection(('127.0.0.1', server.port), timeout=1)
            try:
                with urllib.request.urlopen(
                        f'http://127.0.0.1:{server.port}/callback?code=ok&state=valid', timeout=1) as response:
                    self.assertEqual(response.status, 200)
                closer = threading.Thread(target=server.close, daemon=True)
                closer.start()
                closer.join(1)
                self.assertFalse(closer.is_alive())
            finally:
                idle.close()

    def test_rejects_invalid_state_then_accepts_valid_callback(self):
        with CallbackServer('http://localhost:0/callback', 'valid') as server:
            port = server.server.server_address[1]
            thread = threading.Thread(target=server.wait, kwargs={'timeout': 3})
            thread.start()
            with self.assertRaises(urllib.error.HTTPError) as caught:
                urllib.request.urlopen(f'http://127.0.0.1:{port}/callback?code=x&state=bad')
            caught.exception.close()
            response = urllib.request.urlopen(f'http://127.0.0.1:{port}/callback?code=ok&state=valid')
            self.assertEqual(response.status, 200)
            self.assertIn('text/html', response.headers['Content-Type'])
            body = response.read().decode()
            self.assertIn('请返回终端查看最终结果', body)
            self.assertIn('id="countdown">3</span>', body)
            self.assertIn('let seconds = 3;', body)
            self.assertIn('window.close()', body)
            self.assertNotIn('code=ok', body)
            response.close()
            thread.join(4)
            self.assertEqual(server.code, 'ok')

    def test_callback_remains_responsive_after_authorization(self):
        with CallbackServer('http://localhost:0/callback', 'valid') as server:
            port = server.port
            url = f'http://127.0.0.1:{port}/callback?code=first&state=valid'
            # No wait() call is needed for the receiver to serve requests.
            with urllib.request.urlopen(url, timeout=1) as response:
                self.assertEqual(response.status, 200)
            self.assertEqual(server.wait(timeout=1), 'first')
            with urllib.request.urlopen(url.replace('first', 'repeated'), timeout=1) as response:
                self.assertEqual(response.status, 200)
            self.assertEqual(server.code, 'first')
        self.assertEqual(server.server.fileno(), -1)

    def test_rejects_non_loopback(self):
        with self.assertRaises(ValueError):
            CallbackServer('http://example.com:8765/callback', 'state')

    def test_timeout_releases_server(self):
        with CallbackServer('http://localhost:0/callback', 'valid') as server:
            with self.assertRaises(TimeoutError):
                server.wait(timeout=0.01)

    def test_replaces_owned_listener_and_releases_port(self):
        from core.core.account.callback import CallbackServer as AccountCallback
        first = AccountCallback('http://localhost:0/callback', 'a')
        port = first.server.server_address[1]
        second = AccountCallback(f'http://localhost:{port}/callback', 'b')
        try:
            self.assertEqual(first.server.fileno(), -1)
            self.assertNotEqual(second.server.fileno(), -1)
        finally:
            second.close()
        import socket
        with socket.socket() as sock:
            sock.bind(('127.0.0.1', port))
