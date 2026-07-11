from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DEFAULT_PROVIDER: str = "ollama"

    OLLAMA_BASE_URL: str

    OLLAMA_MODEL: str

    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()