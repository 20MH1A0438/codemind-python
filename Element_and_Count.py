n=int(input())
l=list(map(int,input().split()))
lis=[]
for i in l:
    if i not in lis:
        print(i,l.count(i),end=' ')
        lis.append(i)