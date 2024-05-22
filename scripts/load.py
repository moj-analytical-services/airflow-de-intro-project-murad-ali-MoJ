
from config import Settings
import utils
import boto3
import pandas as pd
from pathlib import Path
from arrow_pd_parser import reader
class S3FileLoade:
    def __init__(self, config:Settings) -> None:
       self.config = config
       s3 = boto3.client('s3')
       data_frame = []

       response = s3.list_objects_v2(Bucket=self.config.BUCKET_NAME, Prefix=self.config.FOLDER_PATH)
       file_paths = [obj['Key']for obj in response.get('Contents')]
       for file_path in file_paths:
            if file_path.endswith('/'):
                continue
            file_path = f"s3://{self.config.BUCKET_NAME}/{file_path}"
            path = Path(file_path)
            if path.suffix =='.parquet':
                df = reader.parquet.read(file_path)
                data_frame.append(df)

       full_df =pd.concat(data_frame, ignore_index = True)
       print(self.config.metadata)
       return full_df    
setting = Settings()
loader = S3FileLoade(setting)



