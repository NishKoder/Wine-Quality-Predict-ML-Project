import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] - %(levelname)s - %(name)s - %(message)s'
)

project_name = "wineQuality"

list_of_dir = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/prediction.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_data_validation.py",
    f"src/{project_name}/pipeline/stage_03_data_transformation.py",
    f"src/{project_name}/pipeline/stage_04_model_trainer.py",
    f"src/{project_name}/pipeline/stage_05_model_evaluation.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for filepath_str in list_of_dir:
    filepath = Path(filepath_str)

    # Ensure the directory exists
    if not filepath.parent.exists():
        filepath.parent.mkdir(parents=True, exist_ok=True)
        logging.info(
            f"Created directory: {filepath.parent} for the file: {filepath.name}"
        )

    # Check if file exists and is not empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()  # This creates an empty file if it doesn't exist
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
