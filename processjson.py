import json

inputfilename = 'uptimerobot.json'

with open(inputfilename, 'r') as inputfile:
    jsondata = inputfile.read()

# print(inputfilename, jsondata, type(jsondata))

# jsonfile = open(inputfilename, 'r')
# jsondata = jsonfile.read()
# print(jsondata)

decoded = json.loads(jsondata)

# pretty printing of json-formatted string
print(json.dumps(decoded, sort_keys=True, indent=4))

print("JSON parsing example: ", decoded['monitors'])
print("Complex JSON parsing example: ", decoded['monitors'][0]['friendly_name'])
for check in range(len(decoded['monitors'])):
    print("Monitor is:", decoded['monitors'][check]['friendly_name'])
print(len(decoded['monitors']))
