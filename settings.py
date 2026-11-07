from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    base_url: str = "https://petstore.swagger.io/v2"


base_settings = Settings()
