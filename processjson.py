import json

inputfilename = 'uptimerobot.json'
inputfilename100 = 'uptimerobot100.json'
inputfilename150 = 'uptimerobot150.json'
inputfilename200 = 'uptimerobot200.json'
outputfilename = 'uptimerobotmonitors.txt'

def printmonitors(inputfilename, outputfilename=outputfilename):
    with open(inputfilename, 'r') as inputfile:
        jsondata = inputfile.read()
    outputfile = open(outputfilename, 'a')
    decoded = json.loads(jsondata)
    for check in range(len(decoded['monitors'])):
        monitorname = decoded['monitors'][check]['friendly_name']
        print("Monitor is:", monitorname)
        outputfile.write(monitorname + '\n')
    print(len(decoded['monitors']))

printmonitors(inputfilename)
printmonitors(inputfilename100)
printmonitors(inputfilename150)
printmonitors(inputfilename200)

