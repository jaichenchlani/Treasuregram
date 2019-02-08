import json
import logging

# Load Configurations
with open('config.json') as config_json_data_file:
    configData = json.load(config_json_data_file)
if configData['env'] == "prod":
    envVariables = configData['prodVariables']
else:
    envVariables = configData['devVariables']

# Setup Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('treasuregram.log')
formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
if envVariables['loggingLevel'] == "high":
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

logger.info("Environment Variables:{0}".format(envVariables))