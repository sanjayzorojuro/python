import heapq

def dih(graph,start):
    queue = [(0,start)]
    distances = {vertex:float('inf')for vertex in graph}
    distances[start] = 0

    while queue:
        curr_dis,curr_node = heapq.heappop(queue)
        if curr_dis > distances[curr_node]:
            continue
        for neig,weight in graph[curr_node]:
            distance = curr_dis + weight
            if distance < distances[neig]:
                distances[neig] = distance
                heapq.heappush(queue,(distance,neig))
    return distances

graph = {
    'a':[('b',3),('c',6)],
    'b':[('c',4),('d',4)],
    'c':[('d',8),('e',5)],
    'd':[('e',3)],
    'e':[],    
}

source = 'a'

print("Dijkastra shortest path:")
dis = dih(graph,source)
for vertex in dis:
    print(f'{source}--{vertex}-->{dis[vertex]}')

