n=int(input())
l=list(map(int,input().split()))
res=0
for i in l:
    if i%2:
        res+=i
    else:
        break
print(res)
        