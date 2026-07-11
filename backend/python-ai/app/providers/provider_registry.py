from app.providers.ollama_provider import OllamaProvider
from app.providers.openai_provider import OpenAIProvider

PROVIDER_REGISTRY = {
    "ollama": OllamaProvider,
    "openai": OpenAIProvider,
}