import json
import csv
'''
Run this app.py to create the json files
Then run processjson.py to create a csv
'''
inputfilename = 'uptimerobot.json'
inputfilename100 = 'uptimerobot100.json'
inputfilename150 = 'uptimerobot150.json'
inputfilename200 = 'uptimerobot200.json'
outputfilename = 'uptimerobotmonitors.txt'
contactsfilename = 'contacts.csv'
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


def getcontactalerts(inputfilename, contactsdictionary, outputfilename=outputfilename):
    with open(inputfilename, 'r') as inputfile:
        jsondata = inputfile.read()
    outputfile = open(outputfilename, 'a', newline='')
    outputfile = csv.writer(outputfile, quoting=csv.QUOTE_ALL)
    decoded = json.loads(jsondata)
    allsmscontacts = []
    for check in range(len(decoded['monitors'])):
        monitorname = decoded['monitors'][check]['friendly_name']
        smscontact = []
        smscontact.append(monitorname)
        contacts = decoded['monitors'][check]['alert_contacts']
        smscontacts = [contact for contact in contacts if contact['type'] == 8]
        for item in smscontacts:
            contactinfo = item['threshold'], contactsdictionary[item['value']]
            smscontact.append(contactinfo)
        allsmscontacts.append(smscontact)
        outputfile.writerow(smscontact)
    return allsmscontacts

printmonitors(inputfilename)
printmonitors(inputfilename100)
printmonitors(inputfilename150)
printmonitors(inputfilename200)

uptimecontacts = getcontacts(contactsfilename)
print(uptimecontacts)
getcontactalerts(inputfilename, uptimecontacts, smscontactsfilename)
getcontactalerts(inputfilename100, uptimecontacts, smscontactsfilename)
getcontactalerts(inputfilename150, uptimecontacts, smscontactsfilename)
getcontactalerts(inputfilename200, uptimecontacts, smscontactsfilename)
