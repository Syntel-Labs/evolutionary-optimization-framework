"""Configuracion central del motor.

Todas las variables de entorno se consumen a traves de este modulo.
Ningun valor debe vivir hardcodeado en codigo: si el entorno no provee
un valor, se usa el default documentado aqui y en .env.example.
"""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class EngineSettings(BaseSettings):
    """Settings del motor leidos desde variables de entorno."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    engine_port: int = Field(default=8000, ge=1, le=65535)
    engine_log_level: str = Field(default="info")
    engine_cors_origins: str = Field(default="http://localhost:3000")
    engine_ilp_default_time_limit: int = Field(default=3600, ge=1)
    engine_ga_workers: int = Field(default=0, ge=0)
    database_url: str = Field(default="")

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.engine_cors_origins.split(",") if o.strip()]


settings = EngineSettings()
