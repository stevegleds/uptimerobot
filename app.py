import requests
import json

def createjsonfile(outputfile, jsondata):
    with open(outputfile, 'w') as outputfile:
        for line in jsondata:
            outputfile.write(line)
    outputfile.close()

url = "https://api.uptimerobot.com/v2/getMonitors"
payload = "api_key=u224617-8424961412fe0f4c596425b0&format=json&logs=1&offset=0&alert_contacts=1"
payload100 = "api_key=u224617-8424961412fe0f4c596425b0&format=json&logs=1&offset=51&alert_contacts=1"
payload150 = "api_key=u224617-8424961412fe0f4c596425b0&format=json&logs=1&offset=101&alert_contacts=1"
payload200 = "api_key=u224617-8424961412fe0f4c596425b0&format=json&logs=1&offset=151&alert_contacts=1"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}

response = requests.request("POST", url, data=payload, headers=headers)
response100 = requests.request("POST", url, data=payload100, headers=headers)
response150 = requests.request("POST", url, data=payload150, headers=headers)
response200 = requests.request("POST", url, data=payload200, headers=headers)


# print(type(response.text))
# print(response.text)
# print(response)
pythondict = json.loads(response.text)
jsondata = json.dumps(pythondict, indent=4)
outputfilename = 'uptimerobot.json'
createjsonfile(outputfilename, jsondata)

pythondict100 = json.loads(response100.text)
jsondata100 = json.dumps(pythondict100, indent=4)
outputfilename100 = 'uptimerobot100.json'
createjsonfile(outputfilename100, jsondata100)

pythondict150 = json.loads(response150.text)
jsondata150 = json.dumps(pythondict150, indent=4)
outputfilename150 = 'uptimerobot150.json'
createjsonfile(outputfilename150, jsondata150)

pythondict200 = json.loads(response200.text)
jsondata200 = json.dumps(pythondict200, indent=4)
outputfilename200 = 'uptimerobot200.json'
createjsonfile(outputfilename200, jsondata200)



# print(pythondict)
# print(type(jsondata))

