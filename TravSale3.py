#Welcome Professor Kumar to my third attempt at this problem
#I've made a lot of comments so hopefully you can catch yourself up quicker

import sys
import multiprocessing as mp
#reading data from file

pool = mp.Pool(mp.cpu_count())

f = open("final_flights35.txt")

listofcities = []
listofedges = []

lines = f.readlines()
for line in lines[1:]:
    line = line.split()
    if line[0] not in listofcities:

        if line[0] == "DFW":
            listofcities.insert(0,line[0])
        else:
            listofcities.append(line[0])
    if line[1] not in listofcities:

        if line[1] == "DFW":
            listofcities.insert(0,line[1])
        else:
            listofcities.append(line[1])


    listofedges.append((listofcities.index(line[0]), listofcities.index(line[1]), int(line[2])))

V = len(listofcities)
src = listofcities.index("DFW")

'''creating nxn adjacency matrix to represent the graph
note that I am treating this graph as directed and am using
sys.maxsize to represent an edge that either does not exist
or does not exist in that direction'''
matrix = []
for i in range(V):
    matrix.append([])
    for j in range(V):
        if i == j:
            matrix[i].append(0)
        else:
            matrix[i].append(sys.maxsize)

f.seek(0)
for line in lines[1:]:
    line = line.split()
    matrix[listofcities.index(line[0])][listofcities.index(line[1])] = int(line[2])

f.close()

'''this is a fuction you can call that will print out any symmetric
matrix in a way that is more readable than printing the list
on it's own. I would recommend using it if you try to print
out any matrices'''
def printmatrix(matrix):
    V = len(matrix[0])
    for i in range(V):
        print("[", end="")
        for j in range(V):
            print(str(matrix[i][j] if matrix[i][j] != sys.maxsize else 'inf') + ", ", end='')
        print("]")

###########################################################################################

'''this is code I copied to emulate the next_permutation
function in C++, as it doesn't exist in Python'''
def next_permutation(L):
    '''
    Permute the list L in-place to generate the next lexicographic permutation.
    Return True if such a permutation exists, else return False.
    '''

    n = len(L)

    # ------------------------------------------------------------

    # Step 1: find rightmost position i such that L[i] < L[i+1]
    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1

    if i == -1:
        return False

    # ------------------------------------------------------------

    # Step 2: find rightmost position j to the right of i such that L[j] > L[i]
    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1

    # ------------------------------------------------------------

    # Step 3: swap L[i] and L[j]
    L[i], L[j] = L[j], L[i]

    # ------------------------------------------------------------

    # Step 4: reverse everything to the right of i
    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True

'''this is the Traveling Salesman Problem algorithm transcribed from the
geeksforgeeks weblink you sent me. I have tested it and it works.
To run it, you must pass in an nxn integer matrix and integer "source"'''
def tsp(graph, src):
    vertex = []
    for i in range(len(graph[0])):
        if i != src:
            vertex.append(i)

    min_pathweight = sys.maxsize
    min_path = [sys.maxsize]

    #do start
    while True:
        current_pathweight = 0
        current_path = []

        k = src
        for i in range(len(vertex)):
            current_pathweight += graph[k][vertex[i]]
            current_path.append([k,vertex[i]])
            k = vertex[i]
        current_pathweight += graph[k][src]
        current_path.append([k,src])
        current_path.append(current_pathweight)

        min_pathweight = min(min_pathweight, current_pathweight)
        check1 = int(min_path[len(min_path)-1])
        check2 = int(current_path[len(current_path)-1])

        minimum = min(check1, check2)
        if minimum == check2:
            min_path = current_path

    #do end
        #while start
        if not next_permutation(vertex):
            break
        #while end

    if min_pathweight >= sys.maxsize:
        return "no path"
    else:
        #return min_pathweight
        return min_path

'''this was the example matrix used on the geeksforgeeks website
that returns 80'''
gfgmatrix = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]

'''Comment this later asdfoghjkfdfljk;hgfdsgjkljhgfgFCVASDFNLASGHNLASDUFASDOUHFDSOIS;O
'''
def tsp_to_cities(result):
    if result == "no path":
        return result
    else:
        cities_result = []
        for r in result[:len(result)-1]:
            thing1 = listofcities[r[0]]
            thing2 = listofcities[r[1]]
            cities_result.append([thing1, thing2])
        cities_result.append(result[len(result)-1])
        return cities_result

'''I wrote this loop to find the minimum number of
vertices/airports > 4 required to make this stupid thing work.
As it turns out, that number is 10.'''
def check_min_solution(matrix):
    for i in range(4,len(matrix)):
        print("Evaluating matrix trimmed to: ", i, "x", i)
        testm = matrix[:i]
        testmatrix = []
        for e in testm:
            testmatrix.append(e[:i])

        #printmatrix(testmatrix)

        #result = tsp(testmatrix, 0)
        result = pool.apply(tsp, args=(testmatrix, 0))
        if result != "no path":
            print("SUCCESS! at: ", i, "x", i)
            result = tsp_to_cities(result)
            print(result, "miles is the minimum distance")
            #break

#print(tsp(gfgmatrix, 0))
#printmatrix(matrix)

check_min_solution(matrix)