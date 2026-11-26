"""Loopback receiver responsive through authorization and shutdown countdown."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit
from ...link.oura_v2.api import validate_callback
import threading

SUCCESS_PAGE = """<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>授权回调已收到</title>
<style>body{font-family:system-ui,sans-serif;background:#f5f7f5;color:#263a30;display:grid;place-items:center;min-height:100vh;margin:0}main{padding:2rem;text-align:center;max-width:32rem}p{line-height:1.6;color:#52635b}</style></head>
<body><main><h1>已收到授权回调</h1><p>正在完成登录，请返回终端查看最终结果。</p>
<p>此页面将在 <span id="countdown">3</span> 秒后尝试关闭。如果没有自动关闭，请手动关闭此标签页。</p></main>
<script>
history.replaceState(null, '', location.pathname);
let seconds = 3;
const timer = setInterval(() => {
  seconds -= 1;
  document.getElementById('countdown').textContent = seconds;
  if (seconds <= 0) { clearInterval(timer); window.close(); }
}, 1000);
</script></body></html>"""

_owners = {}
_lock = threading.RLock()


class CallbackServer:
    def __init__(self, redirect, state):
        parsed = urlsplit(redirect)
        if (parsed.scheme != 'http' or parsed.hostname not in ('localhost', '127.0.0.1')
                or parsed.port is None or parsed.query or parsed.fragment or parsed.username or parsed.password):
            raise ValueError('Callback must be an HTTP localhost URL with a port and no query')
        self.code = None
        self.error = None
        self._ready = threading.Event()
        self._closed = threading.Event()
        self._thread = None
        self._result_lock = threading.Lock()
        receiver = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, format, *args):
                pass  # Never log authorization codes.

            def do_GET(self):
                try:
                    code = validate_callback(f'{parsed.scheme}://{parsed.netloc}{self.path}', redirect, state)
                except ValueError as exc:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(b'Invalid or denied authorization. Return to the application.')
                    if str(exc) == 'Authorization denied or failed':
                        with receiver._result_lock:
                            if receiver.code is None:
                                receiver.error = 'Authorization denied or failed'
                                receiver._ready.set()
                    return
                with receiver._result_lock:
                    if receiver.code is None and receiver.error is None:
                        receiver.code = code
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Cache-Control', 'no-store')
                self.end_headers()
                try:
                    self.wfile.write(SUCCESS_PAGE.encode('utf-8'))
                finally:
                    receiver._ready.set()

        with _lock:
            previous = _owners.get(parsed.port)
            if previous is not None:
                previous.close()
            try:
                self.server = ThreadingHTTPServer(('127.0.0.1', parsed.port), Handler)
            except OSError as exc:
                raise OSError('Callback port is in use by another process') from exc
            self.port = self.server.server_address[1]
            _owners[self.port] = self
    def __enter__(self):
        self._thread = threading.Thread(target=self.server.serve_forever,
                                        kwargs={'poll_interval': 0.1}, daemon=True)
        self._thread.start()
        return self

    def close(self):
        with _lock:
            if self._closed.is_set():
                return
            if self._thread is not None:
                self.server.shutdown()
                self._thread.join()
            self.server.server_close()
            self._closed.set()
            if _owners.get(self.port) is self:
                del _owners[self.port]

    def __exit__(self, *args):
        self.close()

    def wait(self, timeout=60):
        if not self._ready.wait(timeout):
            raise TimeoutError('Authorization callback timed out')
        if self.error:
            raise ValueError(self.error)
        if self.code is None:
            raise TimeoutError('Authorization callback timed out')
        return self.code

