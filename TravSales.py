#from Dijkstra import *
class node:

    def __init__(self, name):
        self.name = name
        self.adjdict = {}
    def getname(self):
        return self.name
    def addcity(self, adjcity):
        #adjcity will be a list with [0] = city name, [1] = distance
        self.adjdict[adjcity[0]] = int(adjcity[1])
    # adjdict has to be a dictionary with keys being cities and values being distances
    def getAdj (self):
        return self.adjdict
    def __str__(self):
        return str("\n***********" + self.name + "***********\nOutgoing Flights To:\n" + str(self.adjdict) + "\n**************************\n")

def printnodes(objs):
    print("[", end="")
    for obj in objs:
        print(obj.getname(), ", ", end="")
    print("]")

cityobjs = []
citynames = []
f = open("final_flights35.txt")

line = f.readlines()[1]
linee = line.split()
cityobjs.append(node(linee[0]))
citynames.append(cityobjs[0].getname())
cityobjs[0].addcity([linee[1], linee[2]])
f.seek(0)

for line in f.readlines()[2:]:
    linee = line.split()
    city = linee[0]
    adjcity = [linee[1], linee[2]]

    if city in citynames:
        cityobjs[citynames.index(city)].addcity(adjcity)
    else:
        cityobjs.append(node(city))
        cityobjs[len(cityobjs) - 1].addcity(adjcity)
        citynames.append(cityobjs[len(cityobjs) - 1].getname())


print(len(cityobjs))
print(cityobjs[0])