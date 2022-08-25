t=int(input())
l=list(map(int,input().split()))
k=0
for i in l:
    if i%2:
        k+=i
print(k)