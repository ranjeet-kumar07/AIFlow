from fastapi import FastAPI

from app.gateway.gateway import LLMGateway
from app.middleware.logging_middleware import LoggingMiddleware
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.exceptions.handlers import (
    template_validation_exception_handler,
)
from app.exceptions.template_validation_error import (
    TemplateValidationError,
)
from app.rag.knowledge_loader import KnowledgeLoader


app = FastAPI(
    title="AIFlow",
    version="1.0.0"
)

app.add_middleware(
    LoggingMiddleware
)

# Load the knowledge base into the vector store
KnowledgeLoader.initialize()

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


app.add_exception_handler(
    TemplateValidationError,
    template_validation_exception_handler
)