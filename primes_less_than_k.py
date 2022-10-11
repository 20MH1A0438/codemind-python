n=int(input())
l=list(map(int,input().split()))
a=int(input())
c=0
for i in l:
    if i==2 and i<=a:
        c+=1
    elif i!=1 and i%2!=0 and i<=a:
        for j in range(3,i//2+1):
            if i%j==0:
                break
        else:
            c+=1
print(c)