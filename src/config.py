from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


load_dotenv()


class DatabaseSettings(BaseSettings, extra='allow'):
    mongo_url: str = "mongodb://localhost:27017"
    db_name: str = "test"

    model_config = SettingsConfigDict(env_file="../.env")

db_settings = DatabaseSettings()
