n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
res=[]
for i in l:
    if int(i)>=a and int(i)<=b:
        res.append(int(i))
if res!=[]:
    print(min(res))
else:
    print(-1)
        