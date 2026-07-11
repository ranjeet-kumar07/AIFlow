from fastapi import FastAPI

from app.gateway.gateway import LLMGateway
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.middleware.logging_middleware import LoggingMiddleware

app = FastAPI(
    title="AIFlow",
    version="1.0.0"
)

app.add_middleware(
    LoggingMiddleware
)

gateway = LLMGateway()


@app.get("/")
def health():

    return {
        "status": "UP",
        "application": "AIFlow"
    }


@app.post(
    "/chat",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest
):

    return gateway.generate_response(request)