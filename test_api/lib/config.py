import os
import yaml

config_path = os.path.join(os.getcwd(), "/home/sysansible/test_api_acmdv_f5/test_api/config.yaml")

f = open(config_path,'r')
config = yaml.safe_load(f)
authen = config["authen"]
api = config["api"]
