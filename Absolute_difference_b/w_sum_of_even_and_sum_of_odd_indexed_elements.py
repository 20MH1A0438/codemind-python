t=int(input())
l=list(map(int,input().split()))
k=l[0]
p=0
for i in range(1,t):
    if i%2==0:
        k+=int(l[i])
    else:
        p+=int(l[i])
print(abs(p-k))