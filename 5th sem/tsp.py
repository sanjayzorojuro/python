from sys import maxsize
from itertools import permutations

v = 4

def tsp(graph,s):
    vertex =[]
    for i in range(v):
        if i != s:
            vertex.append(i)
    minpath = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        print()
        print(i)
        currnetpath = 0
        k = s
        for j in i:
            currnetpath += graph[k][j]
            k = j
        currnetpath += graph[k][s]
        minpath = min(minpath,currnetpath)
        print(currnetpath)
    return minpath


graph = [[0,2,5,7],
         [2,0,8,3],
         [5,8,0,1],
         [7,3,1,0 ]]

s=0

print("Tsp")

for i in graph:
    print(i)

print("Minimum cost:",tsp(graph,s))

    