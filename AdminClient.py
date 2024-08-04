import requests
import json

data = {"3":"[[0,10],[2,9]]"}
data = json.dumps(data)
url = "http://127.0.1.1:3000/GetManagerLeaderIP"
# response = requests.get(url=url,data=b'getLeaderManagerIP')
# response = requests.get(url=url+"GetManagerLeaderIP",data=b'getLeaderManagerIP')

response = requests.post(url=url,data=data)
# response = requests.post(url=url+"GetOTPFromAdmin",data=data)
print(response.content.decode())
# Define the data to be sent in the requests
data = {"3": "[[0,10],[2,9]]"}

# Serialize the data to JSON
json_data = json.dumps(data)

# Define the URL for the backend server
url = "http://127.0.1.1:7011/api/"

# Make a POST request to AddNode endpoint with the JSON data
response_add_node = requests.post(url=url + "AddNode", json=json_data)

# Make a POST request to GetOTPFromAdmin endpoint with the JSON data
response_get_otp = requests.post(url=url + "GetOTPFromAdmin", json=json_data)

# Print the responses from the server
print("AddNode Response:", response_add_node.content.decode())
print("GetOTPFromAdmin Response:", response_get_otp.content.decode())
