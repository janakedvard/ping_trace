from subprocess import PIPE, Popen
import json,sys,datetime
import platform
import csv


with open(sys.argv[1]) as cfile:
    reader = csv.reader(cfile)
    
    temp = []
    for row in reader:
        temp.append(row[1])
        
    data = []
    data = temp[:10]
    data.extend(temp[-10:])
    
 
pings = []
traces = []

for d in data:
    p = Popen(["ping", '-n','10',d], stdout=PIPE)
    ping = p.communicate()[0].decode()
    ps = {
        'target' : d ,
        'output' : ping
    }
    
    pings.append(ps)
    
    t = Popen(["tracert",'-h','30', d], stdout=PIPE)
    trace = t.communicate()[0].decode()
    ts = {
        'target' : d ,
        'output' : trace
    }
    
    traces.append(ts)
    
curDate = datetime.date.today().strftime('%Y%m%d')
opsys = platform.system()
resultPings = {'date' : curDate,
              'system' : opsys,
              'pings' : pings 
             }
resultTraces = {'date' : curDate,
                'system' : opsys,
                'traces' : traces
    }
with open("ping.json", "w") as file:
     json.dump(resultPings,file)

with open("traceroute.json", "w") as file:
    json.dump(resultTraces,file)




    
    
    