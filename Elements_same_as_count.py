n=int(input())
l=list(map(int,input().split()))
c=0
k=[]
for i in l:
    if l.count(i)==i and i not in k:
        c+=1
        k.append(i)
if c==0:
    print(-1)
else:
    for i in k:
        print(i,end=' ')