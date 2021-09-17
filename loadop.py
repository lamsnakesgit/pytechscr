import json
import datetime
import re
#import dateutil

def convert_date(i):
    datetimeobj = datetime.datetime.strptime(i['date'],"%Y-%m-%dT%H:%M:%S.%f")
    d = datetimeobj.strftime("%d.%m.%Y")
    #print(d,'\n')
    return(d)
# amount of digits from end, then if "СЧЕТ" or eng
# if start substring = "Счет"
# find first digits first for cards

def iscardoracc(src):
    if 'Счет' in src:
        acc = "**" + src[:-5:-1]
        return(acc)
    else:
        m = re.search(r"\d", src)
        card = 0
        if m is not None:
            num_index = m.start()
            card = src[num_index:num_index + 4:] + " " + src[num_index + 4:num_index + 6:] + 2 * "*" + " " + 4 * "*" + " "+ src[:-5:-1]
        return(card) #last 4 digits
#    for a in reversed(i):
#        print(a)
#    while i['from'][::-1].isdigit():
#        print(i['from'][::-1].isdigit())
   
with open('operations.json') as file:
    data = json.load(file)
    #op = json.load('operations.json')
# iterate through list state from last: find 5 'executed'
# what is 'last'? defined by time or place in list?
# look at 'date' fields
# format: date + desc + '\n' + from -> to \n + opAm=am+currency
# if account = elif card = frmt 
c = 1
for i in reversed(data):
    if i:
        if i['state'] == 'EXECUTED' and c <= 5: #85 op
            dt = convert_date(i)
            print(dt, i['description'])
            # FROM -> TO card block by 4
            # SUM CURRENCY
            if 'from' in i:
                src = iscardoracc(i['from'])
            else:
                src = '<from>'
            if 'to' in i:
                src2 = iscardoracc(i['to'])
            print(src, src2)
            # SUM CURRENCE
            print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
            print()
            c += 1

