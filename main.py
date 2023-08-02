from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger
STAGE='stage_01 Data ingestion'

try:
    print(f'---------  {STAGE}  started ---------')
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    print(f'---------  {STAGE} completed  ---------')
except Exception as e:
    print(f'---------  {STAGE} failed  ---------')
    logger.exception(e)
    

    