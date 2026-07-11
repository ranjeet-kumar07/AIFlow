from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DEFAULT_PROVIDER: str = "ollama"

    OLLAMA_BASE_URL: str

    OLLAMA_MODEL: str


    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4.1-mini"

    class Config:
        env_file = ".env"


settings = Settings()