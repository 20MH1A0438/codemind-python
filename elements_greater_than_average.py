n=int(input())
l=list(map(int,input().split()))
c=sum(l)//n
res=0
for i in l:
    if i>=c:
        res+=1
print(res)