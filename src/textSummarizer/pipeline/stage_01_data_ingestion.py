from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngetion
from textSummarizer.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager()
        data_ingetion_config=config.get_data_ingetion_config()
        data_ingetion=DataIngetion(data_ingetion_config)
        data_ingetion.download_data()
        data_ingetion.unzip_data()
    