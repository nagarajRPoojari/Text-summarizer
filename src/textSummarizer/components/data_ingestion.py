from urllib import request
from zipfile import ZipFile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import DataIngetionConfig
import os

class DataIngetion:
    def __init__(self,
                 config:DataIngetionConfig):
        
        self.config=config
    
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header=request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{header}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  
            
        
    def unzip_data(self):
        unzip_dir=self.config.unzip_dir
        os.makedirs(unzip_dir,exist_ok=True)
        with ZipFile(self.config.local_data_file,'r') as data_file:
            data_file.extractall(unzip_dir)    
            
            
