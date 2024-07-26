import requests
import json
import time
url = "http://127.0.1.1:10001/GetNextNode"
data = {
    "Source":"http://127.0.1.1:10001/",
    "Current":"http://127.0.1.1:10001/",
    "Destination":"http://127.0.1.1:10006/"
}
data = json.dumps(data)
def route1(): 
    res = requests.post(url=url,data=data)
start = time.time()

route1()

end = time.time()

print(end-start)