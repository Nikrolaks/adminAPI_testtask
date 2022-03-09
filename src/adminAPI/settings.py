import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 5000
    database_url: str = 'sqlite:///' + "C://Users/micro/Nikrolaks/adminAPI_testtask/database.admin.db"


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
