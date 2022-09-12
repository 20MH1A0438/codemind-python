n=int(input())
m=list(map(int,input().split()))
l=[]
for i in m:
    i=str(i)
    l.append(len(i))
k=max(l)
print(l.count(k))
