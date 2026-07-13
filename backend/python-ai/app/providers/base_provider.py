from abc import ABC, abstractmethod

from app.models.provider_request import ProviderRequest
from app.models.chat_response import ChatResponse
from app.models.provider_response import ProviderResponse


class BaseProvider(ABC):

    @abstractmethod
    def generate_response(
        self,
        request: ProviderRequest
    ) -> ProviderResponse:
        pass