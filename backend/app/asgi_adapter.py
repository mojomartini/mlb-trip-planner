"""
Minimal ASGI‑to‑WSGI bridge (embedded version of asgi2wsgi 1.4.4)
— enough to serve FastAPI on PythonAnywhere without the external wheel.
"""

import asyncio
from io import BytesIO

class ASGI2WSGI:
    def __init__(self, asgi_app):
        self.asgi_app = asgi_app

    def __call__(self, environ, start_response):
        # Build basic scope from WSGI environ
        scope = {
            "type": "http",
            "http_version": "1.1",
            "method": environ["REQUEST_METHOD"],
            "path": environ.get("PATH_INFO", ""),
            "raw_path": environ.get("PATH_INFO", "").encode(),
            "query_string": environ.get("QUERY_STRING", "").encode(),
            "headers": [
                (k.lower().encode(), v.encode())
                for k, v in environ.items()
                if k.startswith("HTTP_")
            ],
            "server": (environ.get("SERVER_NAME"), int(environ.get("SERVER_PORT", 80))),
            "client": (environ.get("REMOTE_ADDR"), 0),
            "scheme": environ.get("wsgi.url_scheme"),
        }

        body = environ["wsgi.input"].read(int(environ.get("CONTENT_LENGTH", 0) or 0))
        receive_queue = [{"type": "http.request", "body": body, "more_body": False}]

        async def receive():
            return receive_queue.pop(0)

        send_buffer = BytesIO()
        status_headers = {}

        async def send(message):
            if message["type"] == "http.response.start":
                status_headers["status"] = message["status"]
                status_headers["headers"] = [
                    (k.decode(), v.decode()) for k, v in message.get("headers", [])
                ]
            elif message["type"] == "http.response.body":
                send_buffer.write(message.get("body", b""))

        # Run the ASGI app
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self.asgi_app(scope, receive, send))
        loop.close()

        # Build WSGI response
        status = f"{status_headers.get('status', 200)} OK"
        headers = status_headers.get("headers", [])
        start_response(status, headers)
        return [send_buffer.getvalue()]
