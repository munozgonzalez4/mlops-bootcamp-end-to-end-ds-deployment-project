from src.ds_deployment_project import logger
from src.ds_deployment_project.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.ds_deployment_project.pipeline.data_validation import DataValidationTrainingPipeline
from src.ds_deployment_project.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.ds_deployment_project.pipeline.model_training import ModelTrainingPipeline
from src.ds_deployment_project.pipeline.model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"Stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} completed!")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try: 
    logger.info(f"Stage {STAGE_NAME} started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f"Stage {STAGE_NAME} completed!")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try: 
    logger.info(f"Stage {STAGE_NAME} started")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f"Stage {STAGE_NAME} completed!")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training stage"
try: 
    logger.info(f"Stage {STAGE_NAME} started")
    model_trainer = ModelTrainingPipeline()
    model_trainer.initiate_model_training()
    logger.info(f"Stage {STAGE_NAME} completed!")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation stage"
try: 
    logger.info(f"Stage {STAGE_NAME} started")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.initiate_model_evaluation()
    logger.info(f"Stage {STAGE_NAME} completed!")
except Exception as e:
    logger.exception(e)
    raise e