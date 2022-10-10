n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
res=0
for i in l:
    if int(i)>=a and int(i)<=b:
        print(i,end=' ')
        res=1
if res==0:
    print(-1)
    