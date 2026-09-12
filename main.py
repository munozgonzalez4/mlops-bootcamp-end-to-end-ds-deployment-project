from src.ds_deployment_project import logger
from src.ds_deployment_project.pipeline.data_ingestion import DataIngestionTrainingPipeline

logger.info("Welcome to our custom logger! This is a test log message to demonstrate the logging functionality.")

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"Stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} completed!")
except Exception as e:
    logger.exception(e)
    raise e
