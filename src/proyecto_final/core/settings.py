from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    api_title: str = "Proyecto Final API"

    database_url: str = "sqlite+aiosqlite:///./data/orders.db"

    jwt_secret_key: str = (
        "d59b547c38c5324942f168c9cbf220c766b8d0a5f88391618a9fa11bc5a70b2c"
    )

    jwt_algorithm: str = "HS256"

    access_token_expire_minutes: int = 120

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
