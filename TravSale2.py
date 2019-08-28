from Dijkstra import *

f = open("final_flights35.txt")

listofcities = []
listofedges = []
lines = f.readlines()
for line in lines[1:]:
    line = line.split()
    if line[0] not in listofcities:
        if line[0] == "CHS":
            listofcities.insert(0,line[0])
        else:
            listofcities.append(line[0])
    if line[1] not in listofcities:
        if line[1] == "CHS":
            listofcities.insert(0,line[1])
        else:
            listofcities.append(line[1])

    listofedges.append((listofcities.index(line[0]), listofcities.index(line[1]), line[2]))

V = len(listofcities)
src = listofcities.index("CHS")
print(listofcities.index("CLT"))

graph = Graph(V)
for edge in range(len(listofedges)-1):
    graph.addEdge(listofedges[edge][0], listofedges[edge][1], listofedges[edge][2])
graph.dijkstra(src)