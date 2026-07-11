import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware

from app.middleware.request_context import request_id
from app.utils.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next
    ):

        req_id = str(uuid.uuid4())

        request_id.set(req_id)

        start = time.time()

        logger.info(
            f"[{req_id}] Incoming {request.method} {request.url.path}"
        )

        response = await call_next(request)

        latency = round(
            (time.time() - start) * 1000,
            2
        )

        logger.info(
            f"[{req_id}] Completed in {latency} ms"
        )

        response.headers["X-Request-ID"] = req_id

        return response