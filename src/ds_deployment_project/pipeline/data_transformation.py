from src.ds_deployment_project.config.configuration import ConfigurationManager
from src.ds_deployment_project.components.data_transformation import DataTransformation
from src.ds_deployment_project import logger


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config=ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()


# if __name__ == "__main__":
#     try:
#         logger.info(f"Stage {STAGE_NAME} started...")
#         obj = DataTransformationTrainingPipeline()
#         obj.initiate_data_transformation()
#         logger.info(f"Stage {STAGE_NAME} completed!")
#     except Exception as e:
#         logger.exception(e)
#         raise e