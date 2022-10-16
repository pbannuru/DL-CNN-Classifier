# DL-CNN-CLASSIFIER


## workflow
1.Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config.
6. Update the components
7. Update the pipeline
8. Test run pipeline stage
9. run tox for testing your package
10. Update the dvc.yaml
11. run "dvc repro" for running all the stages in pipeline




git start . # open the file in local system

"""black = wether while creating functions we are following exact standard python structure will be tested with this"""

### tox = test at diff environments
### flake8 = any syntactical mistakes in cod ecan be highlighted by this
# mypy = to check for typing error
# pytest = to run unit test and integration test
# unit test = to test a single function developed

# integration test = to check stages of pipeline together

# bash init_setup.sh

# tox commands:-
1. tox
2. tox --recreate

# venv:
conda activate C:\Users\pbann\DL-CNN-CLASSIFIER\env

# to remove any folder through git command
rm -rf ./env/ 

src\deepClassifier\pipeline\stage_03_training.py

# 
rm ~/.condarc

conda config --set env_prompt '({name})'

conda activate ./env
cd research/mlflow_dir/
dvc dag

<!-- ![]("./docs/images/Data Ingestion).png") -->

![img](https://raw.githubusercontent.com/c17hawke/FSDS_NOV_deepCNNClassifier/main/docs/images/Data%20Ingestion%402x%20(1).png)

# MLflow

STEP 1: Set the env variable | Get it from dagshub -> remote tab -> mlflow tab

MLFLOW_TRACKING_URI=https://dagshub.com/pbannuru/DL-CNN-Classifier.mlflow \
MLFLOW_TRACKING_USERNAME=pbannuru \
MLFLOW_TRACKING_PASSWORD=2c0dd960694539cb43d49fe29cbfe27802bccf34 \


STEP 2: install mlflow

STEP 3: Set remote URI

STEP 4: Use context manager of mlflow to start run and then log metrics, params and model


docker run -p 8501:8501 pred_service

282aad428c79 -docker image id