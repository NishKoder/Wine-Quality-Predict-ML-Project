from pathlib import Path


def create_project_structure(proj_name):
    base_paths = [
        Path(f"src/{proj_name}/components"),
        Path(f"src/{proj_name}/utils"),
        Path(f"src/{proj_name}/config"),
        Path(f"src/{proj_name}/pipeline"),
        Path(f"src/{proj_name}/entity"),
        Path(f"src/{proj_name}/constants"),
        Path("config"),
        Path("research"),
        Path("templates"),
    ]

    files_with_paths = [
        Path(f"src/{proj_name}/__init__.py"),
        Path(f"src/{proj_name}/components/__init__.py"),
        Path(f"src/{proj_name}/components/data_ingestion.py"),
        Path(f"src/{proj_name}/components/data_transformation.py"),
        Path(f"src/{proj_name}/components/data_validation.py"),
        Path(f"src/{proj_name}/components/model_evaluation.py"),
        Path(f"src/{proj_name}/components/model_trainer.py"),
        Path(f"src/{proj_name}/utils/__init__.py"),
        Path(f"src/{proj_name}/utils/common.py"),
        Path(f"src/{proj_name}/config/__init__.py"),
        Path(f"src/{proj_name}/config/configuration.py"),
        Path(f"src/{proj_name}/pipeline/__init__.py"),
        Path(f"src/{proj_name}/pipeline/prediction.py"),
        Path(f"src/{proj_name}/pipeline/stage_01_data_ingestion.py"),
        Path(f"src/{proj_name}/pipeline/stage_02_data_validation.py"),
        Path(f"src/{proj_name}/pipeline/stage_03_data_transformation.py"),
        Path(f"src/{proj_name}/pipeline/stage_04_model_trainer.py"),
        Path(f"src/{proj_name}/pipeline/stage_05_model_evaluation.py"),
        Path(f"src/{proj_name}/entity/__init__.py"),
        Path(f"src/{proj_name}/entity/config_entity.py"),
        Path(f"src/{proj_name}/constants/__init__.py"),
        Path("config/config.yaml"),
        Path("params.yaml"),
        Path("schema.yaml"),
        Path("main.py"),
        Path("app.py"),
        Path("requirements.txt"),
        Path("setup.py"),
        Path("research/trials.ipynb"),
        Path("templates/index.html"),
    ]

    # Create directories
    for path in base_paths:
        path.mkdir(parents=True, exist_ok=True)

    # Create files
    for file_path in files_with_paths:
        file_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
        file_path.touch(exist_ok=True)  # Create file if it doesn't exist, do nothing
        # if it does

    print(f"Project structure for '{proj_name}' created successfully.")


if __name__ == "__main__":
    project_name = "wineQuality"  # Set your project name here
    create_project_structure(project_name)
