a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=[]
for i in l1:
    if (i in l2) and (i not in l):
        l.append(i)
for i in l2:
    if (i in l1) and (i not in l):
        l.append(i)
for i in l:
    print(i,end=' ')
#print(l1,l2)