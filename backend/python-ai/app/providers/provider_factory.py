from app.config.settings import settings
from app.providers.provider_registry import (
    PROVIDER_REGISTRY,
)


class ProviderFactory:

    @staticmethod
    def get_provider(model: str):

        provider_name = (
            settings.DEFAULT_PROVIDER.lower()
        )

        provider_class = PROVIDER_REGISTRY.get(
            provider_name
        )

        if provider_class is None:
            raise ValueError(
                f"Unsupported provider: {provider_name}"
            )

        return provider_class()