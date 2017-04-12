import json
import csv

inputfilename = 'uptimerobot.json'
inputfilename100 = 'uptimerobot100.json'
inputfilename150 = 'uptimerobot150.json'
inputfilename200 = 'uptimerobot200.json'
outputfilename = 'uptimerobotmonitors.txt'
contactsfilename = 'contacts3.csv'
smscontactsfilename = 'smscontacts.csv'

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


def getcontacts(contactsfilename):
    uptimecontacts = {}
    file = open(contactsfilename, newline='')
    contactdata = csv.reader(file)
    header=next(contactdata) # move to first data row
    for row in contactdata:
        uptimecontacts[row[1]] = row[0]
    return uptimecontacts


def printcontacts(inputfilename, contactsdictionary, outputfilename=outputfilename):
    with open(inputfilename, 'r') as inputfile:
        jsondata = inputfile.read()
    outputfile = open(outputfilename, 'a')
    decoded = json.loads(jsondata)
    smscontacts = []
    for check in range(len(decoded['monitors'])):
        monitorname = decoded['monitors'][check]['friendly_name']
        print("Monitor is:", monitorname)
        contacts = decoded['monitors'][check]['alert_contacts']
        smscontacts = [contact for contact in contacts if contact['type'] == 8]
        # print(type(smscontacts), smscontacts)
        for item in smscontacts:
            print('first item is', type(item['value']), item['threshold'], contactsdictionary[item['value']])
        print(type(contacts), contacts)
    return smscontacts

printmonitors(inputfilename)
printmonitors(inputfilename100)
printmonitors(inputfilename150)
printmonitors(inputfilename200)

uptimecontacts = getcontacts(contactsfilename)
print(uptimecontacts)
printcontacts(inputfilename, uptimecontacts, smscontactsfilename)

