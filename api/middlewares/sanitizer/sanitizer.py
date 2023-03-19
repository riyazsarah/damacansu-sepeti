import html

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from starlette.types import Message


async def set_body(request: Request, body: bytes):
    async def receive() -> Message:
        return {
            "type": "http.request",
            "body": body,
        }

    request._receive = receive


class SanitizerMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app,
        some_attribute: str,
    ):
        super().__init__(app)
        self.some_attribute = some_attribute

    async def dispatch(self, request: Request, call_next):
        body = await request.body()
        html.escape(body.decode("utf-8").replace("&", "&amp;"))
        await set_body(request, body)
        # process the request and get the response
        response = await call_next(request)
        return response
