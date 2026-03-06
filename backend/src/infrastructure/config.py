from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost:5432/app"
    FRONTEND_URL: str = "http://localhost:3000"

    model_config = {"env_file": ".env"}


settings = Settings()
