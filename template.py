import os 
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO,format="[%(asctime)s] :%(message)s:")

project_name="textSummarization"

list_of_file=[
    
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "setup.py",
    "requirements.txt",
    "config/config.yaml",
    "params.yaml",
    "research/trial.ipynb",
    "main.py",
    "app.py",
    "Dockerfile"
]

for filepath in list_of_file:
    filepath=Path(filepath)
    file_dir, file_name =os.path.split(filepath)
    
    if file_dir !='':
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating Directory :{file_dir}  for the file {file_name}")


    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath,'w')as f:
            pass
            logging.info(f"Crating empty file {filepath}")
    
    else:
        logging.info(f"{filepath} file is already exist")
    
    