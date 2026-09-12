import os
import urllib.request as request
import zipfile

from src.ds_deployment_project import logger
from src.ds_deployment_project.entity.config_entity import DataIngestionConfig


# Components
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Data downloaded and saved to {self.config.local_data_file}")
        else:
            logger.info(f"Data already exists at {self.config.local_data_file}")

    def download_data(self):
        self.download_file()

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)