n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
k=[]
for i in l:
    if i<a:
        k.append(i)
        c+=1
    elif i>a and i>b:
        k.append(i)
        c+=1
if c==0:
    print(-1)
else:
    print(min(k))
