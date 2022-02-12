# This example requires the requests library be installed.  You can learn more
# about the Requests library here: http://docs.python-requests.org/en/latest/

from requests import get
import json

ip = get('https://api.ipify.org').text
print ('My public IP address is:', ip)

#data to be writtern
address = {
    "ip": ip
}

# Serializing json 
json_object = json.dumps(address, indent = 1)
  
# Writing to sample.json
with open("./src/ip.json", "w") as outfile:
    outfile.write(json_object)

