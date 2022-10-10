n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
res=0
c=0
for i in l:
    if i>res and i<a:
        res=i
        c+=1
    elif i>res and i>a and i>b:
        res=i
        c+=1
if c==0:
    print(-1)
else:
    print(res)