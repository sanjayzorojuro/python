x=[[9,6],[1,5]]
y=[[8,7],[3,4]]
z=[[0,0],[0,0]]

print("First matrix is:")
for i in x:
    print(i)

print("The second matrix is:")
for i in y:
    print(i)

m1=(x[0][0]+x[1][1])*(y[0][0]+y[1][1])
m2=(x[1][0]+x[1][1])*y[0][0]
m3=x[0][0]*(y[0][1]-y[1][1])
m4=x[1][1]*(y[1][0]-y[0][0])
m5=(x[0][0]+x[0][1])*y[1][1]
m6=(x[1][0]-x[0][0])*(y[0][0]+y[0][1])
m7=(x[0][1]-x[1][1])*(y[1][0]+y[1][1])

z[0][0]=m1+m4-m5+m7
z[0][1]=m3+m5
z[1][0]=m2+m4
z[1][1]=m1-m2+m3+m6

print("The final matrix is :")
for i in z:
    print(i)



