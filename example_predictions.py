# import dependencies
import numerapi
import os
import yaml

# Load your API keys and model from config.yml
with open("config.yml", "r") as yml:
    numerai_conf = yaml.safe_load(yml)

# Set your API keys and model_id
public_id = numerai_conf["public_id"]
secret_key = numerai_conf["secret_key"]
model_id = numerai_conf["model_id"]

napi = numerapi.NumerAPI(public_id=public_id, secret_key=secret_key, verbosity="info")
current_round = napi.get_current_round()
path_numerai_dataset = f'numerai_dataset_{current_round}'

# Download and unzip the tournament dataset of current round
if not os.path.isdir(path_numerai_dataset):
  napi.download_current_dataset(unzip=True)

# Upload example_predictions.csv
submission_id = napi.upload_predictions(f'{path_numerai_dataset}/example_predictions.csv', model_id=model_id)
