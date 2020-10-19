#Solution to https://www.youtube.com/watch?v=qz9tKlF431k&t=219s

def makinglist():
    for i in r:
        b = r[i]
        for j in b:
            try:
                if r[j] != ['0']:
                    a = r[i]
                    if i in r[j]:
                        c = r[j][:]
                        del c[r[j].index(i)]
                        a = a + c
                        r[i] = a
                    else:
                        a = a + r[j]
                        r[i] = a
            except:
                pass

def twoconnectionstest():
    global c
    global d
    d = []
    c = 1
    for i in range(17):
        for j in range(17):
            if len(dict.fromkeys(r[airports[i]] + r[airports[j]])) == 15:
                d.append([airports[i], airports[j]])
                c = 2

def threeconnectionstest():
    global c
    global d
    d=[]
    for i in range(17):
        for j in range(17):
            for k in range(17):
                if len(dict.fromkeys(r[airports[i]] + r[airports[j]] + r[airports[k]])) == 14:
                    d.append([airports[i], airports[j], airports[k]])
                    c = 2

airports = ['BGI','CDG','DEL','DOH','DSM','EWR','EYW','HND','ICN','JFK','LGA','LHR','ORD','SAN','SFO','SIN','TLV','BUD']
routes = [
['DSM','ORD'],
['ORD','BGI'],
['BGI','LGA'],
['SIN','CDG'],
['CDG','SIN'],
['CDG','BUD'],
['DEL','DOH'],
['DEL','CDG'],
['TLV','DEL'],
['EWR','HND'],
['HND','ICN'],
['HND','JFK'],
['ICN','JFK'],
['JFK','LGA'],
['EYW','LHR'],
['LHR','SFO'],
['SFO','SAN'],
['SFO','DSM'],
['SAN','EYW']
]

r={}
for i in routes:
    try:
        if r[i[0]] != ['0']:
            a = r[i[0]]
            a.append(i[1])
            r[i[0]] = a
    except:
        r[i[0]] = [i[1]]
for i in airports:
    if i not in [keys for keys in r]:
        if i != 'LGA':
            r[i] = []

makinglist()
makinglist()
for key,value in r.items():
    a = list(dict.fromkeys(value))
    if key in a:
        b = a.index(key)
        del a[b]
    if 'LGA' in a:
        b = a.index('LGA')
        del a[b]
    r[key] = a
print(r)
del airports[airports.index('LGA')]
twoconnectionstest()
if c != 2:
    threeconnectionstest()
    if c != 2 :
        print("More connections test is needed")
    else:
        print("Successful! Minimum Connections Required is 3")
        print(d)
        e = d[:]
        for i in range(len(e)):
            for j in range(i+1,len(e)):
                if e[i][0] in e[j] and e[i][1] in e[j] and e[i][2] in e[j]:
                    try:
                        del d[d.index(e[j])]
                    except:
                        pass
        print("The list of three possible airports from LGA to reach any other airports are:",d)


else:
    print("Successful! Minimum Connections Required is 2")
    print(d)








