import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response = urlopen("HTTP://freeeoip.net/json/"+ipAddress).read().decode('UTF-8')
    responseJson = json.loads(response)
    return responseJson.get("Country_code")

print(getCountry("50.78.253.58"))