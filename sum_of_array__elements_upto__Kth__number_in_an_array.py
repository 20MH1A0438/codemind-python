n=int(input())
l=list(map(int,input().split()))
a=int(input())
res=0
for i in range(n):
    if l[i]<=a:
        res+=l[i]
    else:
        break
print(res)
        