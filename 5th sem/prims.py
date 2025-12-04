inf = 9999
N = 5
sum = 0
G=[[0,19,5,0,0],
   [19,0,5,9,2],
   [5,5,0,1,6],
   [0,9,1,0,1],
   [0,2,6,1,0]
   ]

visited= [0,0,0,0,0]
edge = 0
visited[0] = True

print("The prims weights are:")
for i in G:
    print(i)
 
print("The min cost spanning tree is:")
print("\n edge \t:\t weight\n")

while edge < N-1:
    mini = inf
    a = 0
    b = 0
    for i in range(N):
        if visited[i]:
            for j in range(N):
                if ((not visited[j])and G[i][j]):
                    if mini > G[i][j]:
                        mini = G[i][j]
                        a=i
                        b=j
    print(f"{a} \t :\t{b} \t=\t{G[a][b]}")
    sum += G[a][b]
    visited[b] = True
    edge+=1

print(sum)

