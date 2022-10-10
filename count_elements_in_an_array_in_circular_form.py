n=int(input())
l=list(map(int,input().split()))
l=l+l
count=0
for i in range(n):
    if (l[i-1]%2 and l[i+1]%2==0) or (l[i-1]%2==0 and l[i+1]%2):
        count+=1
print(count)