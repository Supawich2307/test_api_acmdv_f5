from lib.request import retry_session
from lib.authen_token import token as my_token
# from flatten_json import flatten
# import pandas as pd
# import numpy as np
import json


session = retry_session()
def req_pool(token): 
    url = my_token.find_url("pool")
    headers = {
        "X-F5-Auth-Token": token,
        "Accept": "application/json"
    }
    response = session.get(url=url, headers=headers, verify=False)
    text_res = json.loads(response.text)
    text_dump = json.dumps(text_res,ensure_ascii=False,indent=2)
    print(text_dump)

      
def req_virtual(token):
    url = my_token.find_url("virtual")
    headers = {
        "X-F5-Auth-Token": token,
        "Accept": "application/json"
    }
    response = session.get(url=url, headers=headers, verify=False)
    text_res = json.loads(response.text)
    text_dump = json.dumps(text_res,ensure_ascii=False,indent=2)
    print(text_dump)

def req_node(token):
    url = my_token.find_url("node")
    headers = {
        "X-F5-Auth-Token": token,
        "Accept": "application/json"
    }
    response = session.get(url=url, headers=headers, verify=False)
    text_res = json.loads(response.text)
    text_dump = json.dumps(text_res,ensure_ascii=False,indent=2)
    print(text_dump)

def req_rule(token):
    url = my_token.find_url("rule")
    headers = {
        "X-F5-Auth-Token": token,
        "Accept": "application/json"
    }
    response = session.get(url=url, headers=headers, verify=False)
    text_res = json.loads(response.text)
    text_dump = json.dumps(text_res,ensure_ascii=False,indent=2)
    print(text_dump)


if __name__=='__main__':
    token = my_token().access_token(session)
    req_pool(token)
    req_node(token)
    req_virtual(token)
    req_rule(token)





    # url = my_token.find_url("pool")
    # pool_res = req(url=url,token=token).get()
    # for loop in data["items"]:
    #     kind2 = loop["kind"]
    #     name = loop["name"]
    #     partition = loop["partition"]
    #     fullPath = loop["fullPath"]
    #     generation = loop["generation"]
    #     generation = loop["generation"]/Users/supawich.rom/acmdb/lib/request.py
    #     selfLink = loop["selfLink"]
    #     allowNat = loop["allowNat"]            
    #     allowSnat = loop["allowSnat"]
    #     ignorePersistedWeight = loop["ignorePersistedWeight"]
    #     ipTosToClient = loop["ipTosToClient"]
    #     ipTosToServer = loop["ipTosToServer"]
    #     linkQosToClient = loop["linkQosToClient"]
    #     linkQosToServer = loop["linkQosToServer"]
    #     loadBalancingMode = loop["loadBalancingMode"]
    #     minActiveMembers = loop["minActiveMembers"]
    #     minUpMembers = loop["minUpMembers"]
    #     minUpMembersAction = loop["minUpMembersAction"]
    #     minUpMembersChecking = loop["minUpMembersChecking"]
    #     monitor = loop["monitor"]
    #     queueDepthLimit = loop["queueDepthLimit"]
    #     queueOnConnectionLimit = loop["queueOnConnectionLimit"]
    #     queueTimeLimit = loop["queueTimeLimit"]
    #     reselectTries = loop["reselectTries"]
    #     serviceDownAction = loop["serviceDownAction"]
    #     slowRampTime = loop["slowRampTime"]
    #     link = loop["membersReference"]["link"]
    #     isSubcollection = loop["membersReference"]["isSubcollection"]

    # print(flatten(data))
    





