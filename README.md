# mlops-bootcamp-end-to-end-ds-deployment-project

first step: create environment
conda create -p venv python==3.10 -y
conda activate venv/
Create requirements.txt and pip install -r requirements.txt
Create template.py for project structure and run

Logging is set up in __init__ of src/ds_deployment_project

utils/common.py for common functions 

## Workflows: ML Pipeline
1. Data ingestion
2. Data validation
3. Data transformation
4. Model training
5. Model evaluation -> using MLflow

## Workflow to create a pipeline:
1. Update config/config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity. Entity is the classes that will be used for the pipelines
5. Update the configuration manager in src/project/config/configuration.py
6. Update the components
7. Update the pipeline
8. Update the main.py

## How pipelines work (example for Ingestion Pipeline)
- main.py calls DataIngestionTrainingPipeline class which is defined in src/project/pipeline/data_ingestion.py
- The data_ingestion.py script defines the DataIngestionTrainingPipeline using the ConfigurationManager class defined in src/project/config/configuration for the configuration details, and the DataIngestion class defined in src/project/components/data_ingestion.py where the steps of the pipeline DataIngestion are defined, which of course uses the information in ConfigurationManager. 
- The ConfigurationManager class defined in src/project/config/configuration.py uses as parameters the class DataIngestionConfig, which is defined in the entities (src/project/entity/config_entity.py)
- In general the src/project/utils/common.py are used, along with the src/project/constants/__init__.py
- In general config/config.yaml is used to define paths of the pipeline
- Note: for this example, params.yaml and schema.yaml are not used yet

##

For model evaluation, requires connecting to Dagshub
- Open Dagshub in browser and connect using github credentials
- Integrate github repo
- Configure MLflow tracking URI and DVC secret access keys:
    - Set environment variables that are available in experiments (MLflow tracking URI) and data (setup credentials)
    - Initially, those are in the components/model_evaluation.py, but this will change in the next step


##

Final step: Training and Prediction Pipeline with Flask App
- Creation of prediction.py script in pipelines folder
- Creation of app.py for the Flask API

setup.py: useful to wrap entire project as a package
