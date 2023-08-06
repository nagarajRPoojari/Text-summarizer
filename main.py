from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_train import ModelTrainerPipeline
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
    
STAGE='stage_01 Data validation'
    
    
try:
    print(f'---------  {STAGE}  started ---------')
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    print(f'---------  {STAGE} completed  ---------')
except Exception as e:
    print(f'---------  {STAGE} failed  ---------')
    logger.exception(e)
    
    
    
STAGE='stage_01 Data transformation'

try:
    print(f'---------  {STAGE}  started ---------')
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.main()
    print(f'---------  {STAGE} completed  ---------')
except Exception as e:
    print(f'---------  {STAGE} failed  ---------')
    logger.exception(e)
    
    
STAGE='stage_04 Model training'

try:
    print(f'---------  {STAGE}  started ---------')
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.main()
    print(f'---------  {STAGE} completed  ---------')
except Exception as e:
    print(f'---------  {STAGE} failed  ---------')
    logger.exception(e)