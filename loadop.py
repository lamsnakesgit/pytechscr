import json
import datetime
#import dateutil

#def convert_date():
   
with open('operations.json') as file:
    data = json.load(file)
    #op = json.load('operations.json')
#print(len(data)) #101 
#print(data[:-5]) #5 times?
#print(data[::-5])
#print(data[:-5:])
##print(data[-5:]) # printf x-5,x-4.. until last
# iterate through list state from last: find 5 'executed'
# what is 'last'? defined by time or place in list?
# look at 'date' fields
#print(data[-1]['date'])
c = 0
for i in reversed(data):
# #for i in len(data):
    #print(i)
    if i:
        if i['state'] == 'EXECUTED': #85 op
            #convert_date(i)
            #datetimeobj = datetime.datetime.strptime(i['date'],"%Y-%M-%dT%HH:%MM:%SS.%f")
            #datetimeobj = datetime.datetime.strptime(i['date'],"%Y-%M-%d")
            datetimeobj = datetime.datetime.strptime(i['date'],"%Y-%m-%dT%H:%M:%S.%f")
            ###d = dateutil.parser.parse(i['date'])
            ###print("DUT\n", d, "\n")
            ##i['date'].isoformat()
          #  print(i['date'], "\n")
            #d = datetimeobj.strftime("%D.%M.%Y") #wtf is with D M
            d = datetimeobj.strftime("%d.%m.%Y")
            print(d,'\n')
            #print(i["date"]) #debugged
            #print(i["id"])
            c += 1
