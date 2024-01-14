import json
from sagemaker.huggingface import HuggingFaceModel

# sm conf
instance_type = "ml.g5.48xlarge"
number_of_gpu = 8
health_check_timeout = 300

# model/endpoint conf
config = {
    'HF_MODEL_ID': "mistralai/Mixtral-8x7B-Instruct-v0.1", # model_id from hf.co/models
  'SM_NUM_GPUS': json.dumps(number_of_gpu), # Number of GPU used per replica
  'MAX_INPUT_LENGTH': json.dumps(24000),  # Max length of input text
  'MAX_BATCH_PREFILL_TOKENS': json.dumps(32000),  # Number of tokens for the prefill operation.
  'MAX_TOTAL_TOKENS': json.dumps(32000),  # Max length of the generation (including input text)
  'MAX_BATCH_TOTAL_TOKENS': json.dumps(512000),  # Limits the number of tokens that can be processed in parallel during the generation
}

# create hf model 
llm_model = HuggingFaceModel(
  role=role,
  image_uri=llm_image,
  env=config
)

# Deploy model to an endpoint
llm = llm_model.deploy(
  initial_instance_count=1,
  instance_type=instance_type,
  container_startup_health_check_timeout=health_check_timeout, # 10 minutes to be able to load the model
)