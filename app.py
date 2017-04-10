import requests
import json

url = "https://api.uptimerobot.com/v2/getMonitors"

payload = "api_key=u224617-8424961412fe0f4c596425b0& format = json & logs = 1"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}

response = requests.request("POST", url, data=payload, headers=headers)
print(type(response.text))
print(response.text)
print(response)
pythondict = json.loads(response.text)
jsondata = json.dumps(pythondict, indent=4)
outputfilename = 'uptimerobot.json'

with open(outputfilename, 'w') as outputfile:
    for line in jsondata:
        outputfile.write(line)

outputfile.close()

print(pythondict)
print(type(jsondata))
# print(jsondata)

for item in jsondata:
    print(item, type(item))


