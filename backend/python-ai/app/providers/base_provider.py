from abc import ABC, abstractmethod

from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse


class BaseProvider(ABC):
    """
    Contract that every LLM provider must implement.
    """

    @abstractmethod
    def generate_response(
        self,
        request: ChatRequest
    ) -> ChatResponse:
        """
        Generate a response from an LLM.
        """
        pass