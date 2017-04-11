import json

inputfilename = 'uptimerobot.json'
inputfilename100 = 'uptimerobot100.json'
inputfilename150 = 'uptimerobot150.json'
inputfilename200 = 'uptimerobot200.json'

def printmonitors(inputfilename):
    with open(inputfilename, 'r') as inputfile:
        jsondata = inputfile.read()
    decoded = json.loads(jsondata)
    for check in range(len(decoded['monitors'])):
        print("Monitor is:", decoded['monitors'][check]['friendly_name'])
    print(len(decoded['monitors']))

printmonitors(inputfilename)
printmonitors(inputfilename100)
printmonitors(inputfilename150)
printmonitors(inputfilename200)
