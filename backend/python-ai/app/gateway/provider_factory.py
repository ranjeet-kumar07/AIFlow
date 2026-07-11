from app.config.settings import settings
from app.providers.ollama_provider import OllamaProvider


class ProviderFactory:

    @staticmethod
    def get_provider(model: str):

        provider = settings.DEFAULT_PROVIDER.lower()

        if provider == "ollama":
            return OllamaProvider()

        raise ValueError(
            f"Unsupported provider: {provider}"
        )