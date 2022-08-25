t=int(input())
l=list(map(int,input().split()))
k=0
for i in range(1,t,2):
    k+=int(l[i])
print(k)