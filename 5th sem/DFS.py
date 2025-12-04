#Following is the code for DFS.
graph={
    'a':['b','c'],
    'b':['d','e'],
    'c':['f'],
    'd':[],
    'e':['f','g'],
    'f':[],
    'g':[]
}

visited = set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node,end='\t')
        visited.add(node)
        for neig in graph[node]:
            dfs(visited,graph,neig)

print("Adjency list of the given graph is :")
for k,v in graph.items():
    print(f"{k}:{v}")

print("Here is the followin g DFS graph")
dfs(visited,graph,'a')