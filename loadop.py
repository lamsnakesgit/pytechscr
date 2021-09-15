import json
import datetime
#import dateutil

def convert_date(i):
    datetimeobj = datetime.datetime.strptime(i['date'],"%Y-%m-%dT%H:%M:%S.%f")
    d = datetimeobj.strftime("%d.%m.%Y")
    #print(d,'\n')
    return(d)
   
with open('operations.json') as file:
    data = json.load(file)
    #op = json.load('operations.json')
# iterate through list state from last: find 5 'executed'
# what is 'last'? defined by time or place in list?
# look at 'date' fields
# format: date + desc + '\n' + from -> to \n + opAm=am+currency
c = 1
for i in reversed(data):
    if i:
        if i['state'] == 'EXECUTED' and c <= 5: #85 op
            dt = convert_date(i)
            print(dt, i['description'])
            print()
            c += 1
