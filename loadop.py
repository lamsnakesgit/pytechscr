import json
import datetime
import re

def convert_date(i):
    datetimeobj = datetime.datetime.strptime(i['date'],"%Y-%m-%dT%H:%M:%S.%f")
    d = datetimeobj.strftime("%d.%m.%Y")
    return(d)

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
        return(card)
   
with open('operations.json') as file:
    data = json.load(file)

c = 1
for i in reversed(data):
    if i:
        if i['state'] == 'EXECUTED' and c <= 5:
            dt = convert_date(i)
            print(dt, i['description'])
            if 'from' in i:
                src = iscardoracc(i['from'])
            else:
                src = '<from>'
            if 'to' in i:
                src2 = iscardoracc(i['to'])
            print(src, src2)
            print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
            print()
            c += 1

