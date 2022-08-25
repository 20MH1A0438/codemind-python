t=int(input())
l=list(map(int,input().split()))
for i in range(t-1,-1,-1):
    if int(l[i])%2:
        print(l[i])
        break