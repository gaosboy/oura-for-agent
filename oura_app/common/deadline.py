"""Cross-platform deadline for work that must not perform persistent writes."""
import math
import queue
import threading
import time


def run_with_deadline(work, deadline, interval=2, report=None):
    result = queue.Queue(maxsize=1)
    def run():
        try:
            result.put((True, work()))
        except Exception as exc:
            result.put((False, exc))
    threading.Thread(target=run, daemon=True).start()
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError('Login timed out')
        try:
            success, value = result.get(timeout=min(interval, remaining))
        except queue.Empty:
            if report and deadline - time.monotonic() > 0:
                report(math.ceil(deadline - time.monotonic()))
            continue
        if time.monotonic() >= deadline:
            raise TimeoutError('Login timed out')
        if not success:
            raise value
        return value
