import os
import yaml

config_path = os.path.join(os.getcwd(), "test_api_acmdv_f5/test_api/lib/config.yml")

f = open(config_path)
config = yaml.safe_load(f)
authen = config["authen"]
api = config["api"]
