# Kidney-Disease-Classification


## Workflows
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run ?

### STEPS:

Clone the repository

```bash
https://github.com/bayusuarsa/Kidney-Disease-Classification
```

### STEP 01 - Create a conda enviroment after opening the repository

```bash
conda create -n cnncls pyhton=3.8 -y
```

```bash
conda activate cnncls
```

### STEP 02 - Install the requirements
``` bash
pip install -r requirements.txt
```
```
#### cmd
 - mlflow ul
```

### dagshub
[dagshub](http://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/bayusuarsa/Kidney-Disease-Classification.mlflow \
MLFLOW_TRACKING_USERNAME=bayusuarsa \
MLFLOW_TRACKING_PASSWORD=d254646d967e08f12cf189de78c2c4a9527fd3b8 \
python script.py

run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/bayusuarsa/Kidney-Disease-Classification.mlflow 

export MLFLOW_TRACKING_USERNAME=bayusuarsa

export MLFLOW_TRACKING_PASSWORD=d254646d967e08f12cf189de78c2c4a9527fd3b8


```
