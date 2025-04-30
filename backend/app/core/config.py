from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # ---- database ----
    db_user: str = "YOUR_DB_USER"
    db_password: str = "YOUR_DB_PASSWORD"
    db_host: str = "YOUR_DB_HOST"
    db_name: str = "YOUR_DB_NAME"          # <-- please tell me this name
    # ---- CORS ----
    cors_origins: str = "https://YOUR-TEMP-DOMAIN.com,http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def sqlalchemy_uri(self) -> str:
        return (
            f"mysql+pymysql://{self.db_user}:{self.db_password}"
            f"@{self.db_host}/{self.db_name}?charset=utf8mb4"
        )

settings = Settings()  # loaded at import-time

