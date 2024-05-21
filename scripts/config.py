#from pydantic_settings import BaseSettings
from typing import List, Optional, Union


class Settings():
    AWS_REGION: str = "eu-west-2"
    LOADING_FOLDER: Optional[str] = None
    FILE_NAME: str
    BUCKET_NAME: str = "airflow-intro-test-murad"
    FOLDER_PATH: str = "loaded_data/"