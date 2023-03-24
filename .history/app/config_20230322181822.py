from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname: str = ""
    database_port: str = ""
    database_password: str = ""
    database_name: str = ""
    database_username: str = ""
    secret_key: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    algorithm: str = ""
    access_token_expired_minutes: int

settings = Settings()   