import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "ds_deployment_project"

list_of_files = [
    ".github/workflows/.gitkeep", # Generic file to keep the folder in git
    f"src/{project_name}/__init__.py", # Make src a package -> needed to make this convertible to a package
    f"src/{project_name}/components/__init__.py", # Make components a package 
    f"src/{project_name}/utils/__init__.py", # Make utils a package
    f"src/{project_name}/utils/common.py", # Common functions for the project
    f"src/{project_name}/config/__init__.py", # Make config a package 
    f"src/{project_name}/config/configuration.py", # Configuration file for the project
    f"src/{project_name}/pipeline/__init__.py", # Make pipeline a package
    f"src/{project_name}/entity/__init__.py", # Make entity a package
    f"src/{project_name}/entity/config_entity.py", # Entity class for configuration
    f"src/{project_name}/constants/__init__.py", # Make constants a package
    "config/config.yaml", # Configuration file for the project
    "params.yaml", # Parameters file for the project
    "schema.yaml", # Schema file for the project
    "main.py", # Main entry point for the project
    "Dockerfile", # Dockerfile for containerization
    # requirements.txt was already created in the previous step, so we don't need to create it again
    "setup.py", # Setup file for the project
    # README.md was already created in the previous step, so we don't need to create it again
    "research/research.ipynb", # Jupyter notebook for research and experimentation
    "templates/index.html", # HTML template for the project
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists and is not empty. Skipping file creation.")
