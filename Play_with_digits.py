a=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    for j in str(i):
        c+=int(j)
print(c)