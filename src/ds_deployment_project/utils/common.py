import yaml
from box import ConfigBox # ConfigBox is a class from the box library that allows for dot notation access to dictionary keys, making it easier to work with nested configurations.
from box.exceptions import BoxValueError # BoxValueError is an exception raised when there is an error accessing values in a ConfigBox object.
from ensure import ensure_annotations
import os
import joblib

from src.ds_deployment_project import logger


@ensure_annotations # Decorator to ensure that the function arguments and return types match the specified annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml (str): Path to the yaml file.

    Raises:
        ValueError: If the yaml file is empty or cannot be read.
        BoxValueError: If there is an error accessing values in the ConfigBox.

    Returns:
        ConfigBox: A ConfigBox object containing the contents of the yaml file.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

        if content is None:
            raise ValueError(f"YAML file is empty: {path_to_yaml}")

        logger.info("yaml file: %s loaded successfully", path_to_yaml)
        return ConfigBox(content)
    except BoxValueError as e:
        logger.error("BoxValueError: %s", e)
        raise ValueError(f"BoxValueError: {e}") from e
    except Exception as e:
        logger.error("Error reading the yaml file: %s", e)
        raise ValueError(f"Error reading the yaml file: {e}") from e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, logs the creation of directories.
    """
    for path in path_to_directories:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info("Directory created: %s", path)
        else:
            if verbose:
                logger.info("Directory already exists: %s", path)


@ensure_annotations
def save_json(path: str, data: dict):
    """
    Saves a dictionary as a JSON file.

    Args:
        path (str): Path to save the JSON file.
        data (dict): Dictionary to save as JSON.
    """
    import json
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info("JSON file saved: %s", path)    


@ensure_annotations
def load_json(path: str) -> dict:
    """
    Loads a JSON file and returns its contents as a dictionary.

    Args:
        path (str): Path to the JSON file.
    """
    with open(path, 'r') as f:
        data = json.load(f)
    logger.info("JSON file loaded: %s", path)
    return ConfigBox(data)


@ensure_annotations
def save_bin(path: str, data: object):
    """
    Saves an object as a binary file using pickle.

    Args:
        path (str): Path to save the binary file.
        data (object): Object to save as binary.
    """
    joblib.dump(data, path)
    logger.info("Binary file saved: %s", path)


@ensure_annotations
def load_bin(path: str) -> object:
    """
    Loads a binary file and returns its contents.

    Args:
        path (str): Path to the binary file.
    """
    data = joblib.load(path)
    logger.info("Binary file loaded: %s", path)
    return data