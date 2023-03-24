from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: str = "postgres"
    database_password: str = "postgres"
    database_name: str = "postgres"
    database_username: str = "postgres"
    secret_key: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    algorithm: str

settings = Settings()   