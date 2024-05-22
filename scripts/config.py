#from pydantic_settings import BaseSettings
from typing import List, Optional, Union
from mojap_metadata import Metadata
from utils import s3_path_creator


class Settings():
    AWS_REGION: str = "eu-west-2"
    LOADING_FOLDER: Optional[str] = None
    FILE_NAME: str
    BUCKET_NAME: str = "airflow-intro-test-murad"
    FOLDER_PATH: str = "loaded_data/"
    METADATA_FOLDER: str = "metadata"
    metadata = Metadata(s3_path_creator(BUCKET_NAME,METADATA_FOLDER))
