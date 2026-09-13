# MLOps Bootcamp End-to-End Data Science Deployment Project

This repository is primarily educational: it is designed to teach the structure and thinking behind an end-to-end machine learning project in production-style workflows, rather than to serve as a fully production-optimized application.

The goal is to understand how data, configuration, components, pipelines, model tracking, and deployment fit together in a clean project architecture.

## First steps

1. Create the environment:
   ```bash
   conda create -p venv python==3.10 -y
   conda activate venv/
   ```

2. Create the requirements file and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create the project structure and run the template:
   ```bash
   python template.py
   ```

4. Logging is set up in the package initializer at `src/ds_deployment_project/__init__.py`.

5. `src/ds_deployment_project/utils/common.py` contains the common helper functions used throughout the project.

## Project concept: ML pipeline workflow

This project follows a typical MLOps-oriented workflow:

1. Data ingestion
2. Data validation
3. Data transformation
4. Model training
5. Model evaluation -> using MLflow

The educational idea is that each step is broken into a dedicated stage, with reusable pieces that can be configured and extended.

## Workflow to create a pipeline

When building a new pipeline in this project, the general workflow is:

1. Update `config/config.yaml`
2. Update `schema.yaml`
3. Update `params.yaml`
4. Update the entity. The entity defines the classes that will be used by the pipelines.
5. Update the configuration manager in `src/project/config/configuration.py`
6. Update the components
7. Update the pipeline
8. Update the `main.py`

This pattern is important because it keeps configuration, logic, and execution separate and easier to reason about.

## How the pipelines work (example: ingestion pipeline)

The project is organized around a clear pipeline pattern:

- `main.py` calls the `DataIngestionTrainingPipeline` class, which is defined in `src/project/pipeline/data_ingestion.py`.
- The `data_ingestion.py` pipeline script defines the training pipeline using:
  - the `ConfigurationManager` class from `src/project/config/configuration.py` for configuration details
  - the `DataIngestion` class from `src/project/components/data_ingestion.py` where the actual pipeline steps are implemented
- The `ConfigurationManager` class uses the `DataIngestionConfig` class, which is defined in the entities (`src/project/entity/config_entity.py`).
- The common project helpers live in `src/project/utils/common.py`, along with the constants defined in `src/project/constants/__init__.py`.
- In general, `config/config.yaml` is used to define the file and folder paths for the pipeline.
- Note: for this example, `params.yaml` and `schema.yaml` are not used yet.

This is a good example of the structure used in many ML projects: config files describe the inputs and outputs, entities define expected objects, components implement pieces of logic, and the pipeline orchestrates the execution.

## Model evaluation and Dagshub integration

For model evaluation, the project requires connecting to Dagshub:

- Open Dagshub in the browser and connect using GitHub credentials
- Integrate the GitHub repository
- Configure the MLflow tracking URI and DVC secret access keys:
  - Set environment variables that are available in experiments (MLflow tracking URI) and data (setup credentials)
  - Initially, these are in the `components/model_evaluation.py`, though this will change later as the project evolves

This is a useful learning point because it demonstrates how teams connect experimentation, tracking, and model metadata to a hosted platform rather than just storing results locally.

## Final step: training and prediction pipeline with Flask app

The end of the project introduces a practical deployment pattern:

- Creation of the `prediction.py` script in the pipelines folder
- Creation of the `app.py` file for the Flask API

This shows how a model can be exposed as a service after the training flow is complete.

## Packaging note

`setup.py` is useful for wrapping the entire project as a package. This has not been fully implemented yet, but it is an important concept to keep in mind for packaging and distribution in a real project.

## Summary

This repository is meant to teach the anatomy of a production-style ML pipeline, especially:

- how configuration is centralized
- how code is split into reusable components
- how pipelines orchestrate stages
- how logging and tracking are built into the workflow
- how a model can eventually be served through a Flask application

Even if the functionality is intentionally simple, the architecture is the main lesson. That is the core educational value of this project.