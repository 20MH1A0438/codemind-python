n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(0,n):
    if int(l[i])%2:
        print(l[i],end=' ')
    else:
        m.append(l[i])
for i in m:
    print(i,end=' ')