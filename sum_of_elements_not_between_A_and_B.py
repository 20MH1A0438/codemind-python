n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
count=0
for i in l:
    if i<a:
        count+=int(i)
    elif i>a and i>b:
        count+=int(i)
print(count)
