import sys, logging, logging.config, requests
from os import path

ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
logging.config.fileConfig(path.join(ROOT_DIR ,'logs/loggings.conf'))
log = logging.getLogger("simpleExample")

class ApiRequester():

    def __init__(self):        
        log.info("API Requester initialized")            
    
    def requestUri(self, uri):                
        respons = requests.get(uri)
        log.debug(respons.content)
        log.info(respons.headers)

if __name__ == "__main__":
    api = ApiRequester()
    #'https://jsonplaceholder.typicode.com/todos/1'
    #'https://westeurope.api.cognitive.microsoft.com/sts/v1.0/issueToken'
    uri = "https://jsonplaceholder.typicode.com/todos/1"
    api.requestUri(uri)



    
