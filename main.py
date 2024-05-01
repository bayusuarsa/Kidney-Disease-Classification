from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\n x===============x")
except Exception as e:
    logger.exception(e)



STAGE_NAME = "Prepare base Model"

try:
    logger.info(f'**********************')
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\n x===============x")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Training"

try:
    logger.info(f'**********************')
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    model_trained = ModelTrainingPipeline()
    model_trained.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\n x===============x")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Model Evaluation"

try:
    logger.info(f'**********************')
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    evaluation = EvaluationPipeline()
    evaluation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\n x===============x")
except Exception as e:
    logger.exception(e)
