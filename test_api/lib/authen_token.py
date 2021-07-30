from lib.config import authen,api


class token :
    def __init__(self):
        for finder_authen in authen["user"]:
            self.username = finder_authen["username"]
            self.password = finder_authen["password"]
        for fider_url in api["f5_lb"]:
            self.address = fider_url["address"]
            for loop_uri in fider_url["token"]:
                self.uri = loop_uri["uri"]
        
    def set_header(self):
        self.header = {
            "username": self.username,
            "password": self.password
        }
        return self.header
    def access_token(self,session) :
        response = session.post(url=self.find_url("token"), json=self.set_header(), verify=False)
        for finder in response.json:
            f_token = finder["token"]
            for finder2 in f_token:
                token = finder2["token"]
        print(token)
        return token
    
    def find_url(self,attribute):
        for loop_address in api["f5_lb"]:
            address = loop_address["address"]
            for loop_uri in loop_address[attribute]:
                uri = loop_uri["uri"] 
        print(address+uri)
        return address+uri
        
        
# {
#    "username":"tsm_trainee",
#    "loginReference":{
#       "link":"https://localhost/mgmt/cm/system/authn/providers/local/login"
#    },
#    "loginProviderName":"local",
#    "token":{
#       "token":"2QRECZZDA2QS4ZOUXAIMBSQSUT",
#       "name":"2QRECZZDA2QS4ZOUXAIMBSQSUT",
#       "userName":"tsm_trainee",
#       "authProviderName":"local",
#       "user":{
#          "link":"https://localhost/mgmt/shared/authz/users/tsm_trainee"
#       },
#       "groupReferences":[
         
#       ],
#       "timeout":1200,
#       "startTime":"2021-07-27T18:38:50.822+0700",
#       "address":"10.14.25.3",
#       "partition":"[All]",
#       "generation":1,
#       "lastUpdateMicros":1627385930822551,
#       "expirationMicros":1627387130822000,
#       "kind":"shared:authz:tokens:authtokenitemstate",
#       "selfLink":"https://localhost/mgmt/shared/authz/tokens/2QRECZZDA2QS4ZOUXAIMBSQSUT"
#    },
#    "generation":0,
#    "lastUpdateMicros":0
# }
