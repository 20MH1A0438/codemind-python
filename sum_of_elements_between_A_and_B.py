n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
res=0
for i in l:
    if int(i)>=a and int(i)<=b:
        res+=int(i)
print(res)