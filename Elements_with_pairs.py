n=int(input())
l=list(map(int,input().split()))
if len(l)%2:
    l.append(0)
    for i in l:
        print(i,end=' ')
else:
    for i in l:
        print(i,end=' ')