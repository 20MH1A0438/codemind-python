n=int(input())
l=list(map(int,input().split()))
for i in l:
    print(int(str(i)[::-1]),end=' ')
