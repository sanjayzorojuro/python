def find(parent,node):
    if parent[node] != node:
        parent[node] = find(parent,parent[node])
    return parent[node]

def union(parent,rank,u,v):
    ru = find(parent,u)
    rv = find(parent,v)
    
    if ru == rv:
        return False
    elif rank[ru] < rank[rv]:
        parent[ru] = rv
    elif rank[ru] > rank[rv]:
        parent[rv] = ru
    else:
        parent[rv] = ru
        rank[ru] += 1
    return True

def kurskal(edge,n):
    edge.sort()
    parent = [i for i in range(n)]
    mst = []
    mst_cost = 0
    rank = [0] * n
    for weight,u,v in edge:
        if union(parent,rank,u,v):
            mst.append((u,v,weight))
            mst_cost += weight
    return mst,mst_cost


n = 6
edge=[(4,0,1),
      (4,0,2),
      (2,1,2),
      (5,1,3),
      (1,2,3),
      (3,2,4),
      (6,3,4),
      (7,3,5),
      (8,4,5)
]

mst,cost = kurskal(edge,n)

print("The kurskal solutions are:")
print("Edges are:")
for u,v,weight in mst:
    print(f'{u}--{v}-->{weight}')

print("Total cost",cost)