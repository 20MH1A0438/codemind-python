n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in l:
    if i<a:
        print(i,end=' ')
        c+=1
    elif i>a and i>b:
        print(i,end=' ')
        c+=1
if c==0:
    print(-1)
