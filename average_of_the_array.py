t=int(input())
l=list(map(int,input().split()))
k=0
c=0
for i in l:
    k+=i
    c+=1
print(format(k/c,'.2f'))
    