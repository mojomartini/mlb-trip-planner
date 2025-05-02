"""
Central configuration and SQLAlchemy connection URL builder.
"""

from urllib.parse import quote_plus
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ── database credentials (loaded from .env) ─────────────────
    db_user: str
    db_password: str
    db_host: str
    db_name: str

    # ── CORS origins, comma‑separated ───────────────────────────
    cors_origins: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # ── SQLAlchemy URL with password safely URL‑encoded ─────────
    @property
    def sqlalchemy_uri(self) -> str:
        """
        Build a mysql+pymysql URL, ensuring special characters
        in the password (e.g. '@', ':', '/') are URL‑encoded.
        """
        return (
            "mysql+pymysql://"
            f"{self.db_user}:{quote_plus(self.db_password)}"
            f"@{self.db_host}/{self.db_name}?charset=utf8mb4"
        )


# Singleton settings object imported elsewhere
settings = Settings()
