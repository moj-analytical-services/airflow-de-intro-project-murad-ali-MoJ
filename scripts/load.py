
from config import Settings
import boto3
import pandas as pd
class S3FileLoade:
    def __init__(self, config:Settings) -> None:
       self.config = config
       s3 = boto3.client('s3')
       data_frame = []

       response = s3.list_objects_v2(Bucket=self.config.BUCKET_NAME, Prefix=self.config.FOLDER_PATH)
       path = [obj['Key']for obj in response.get('Contents')]
       print(path)
setting = Settings()
loader = S3FileLoade(setting)



