from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
        cli_parse_args=False
    )
    
    # Database
    postgres_host: str = Field(default="localhost", alias="POSTGRES__HOST")
    postgres_port: int = Field(default=5432, alias="POSTGRES__PORT")
    postgres_user: str = Field(default="postgres", alias="POSTGRES__USER")
    postgres_password: str = Field(default="postgres", alias="POSTGRES__PASSWORD")
    postgres_db: str = Field(default="educational_platform", alias="POSTGRES__DB")

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"


@lru_cache
def get_settings() -> Settings:
    return Settings()
