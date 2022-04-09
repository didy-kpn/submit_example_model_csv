# import dependencies
from numerapi import NumerAPI
from os import environ, path, getcwd
from yaml import safe_load

# Load your API keys and model from config.yml
with open("config.yml", "r") as yml:
    numerai_conf = safe_load(yml)

# Set your API keys and model_id
public_id = numerai_conf["public_id"] if numerai_conf["public_id"] is not None else environ['NUMERAI_PUBLIC_ID']
secret_key = numerai_conf["secret_key"] if numerai_conf["secret_key"] is not None else environ['NUMERAI_SECRET_KEY']
model_id = numerai_conf["model_id"] if numerai_conf["model_id"] is not None else environ['NUMERAI_MODEL_ID']

napi = NumerAPI(public_id=public_id, secret_key=secret_key, verbosity="info")
current_round = napi.get_current_round()
dest_path = numerai_conf["dest_path"] if numerai_conf["dest_path"] is not None else environ['NUMERAI_DEST_PATH']
if not dest_path:
    dest_path=environ['PWD']
path_numerai_dataset = f'{dest_path}/numerai_dataset_{current_round}'

# Download and unzip the tournament dataset of current round
if not path.isdir(path_numerai_dataset):
  napi.download_current_dataset(dest_path=dest_path, unzip=True)

# Upload example_predictions.csv
submission_id = napi.upload_predictions(f'{path_numerai_dataset}/example_predictions.csv', model_id=model_id)
