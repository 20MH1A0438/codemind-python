n=int(input())
m=list(map(int,input().split()))
m=m[::-1]
res=0
for i in range(n):
    res+=int(m[i])*2**i
print(res)
