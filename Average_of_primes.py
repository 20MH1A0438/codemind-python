n=int(input())
l=list(map(int,input().split()))
res=0
c=0
for i in l:
    if i==2:
        res+=i
        c+=1
    elif i!=1 and i%2!=0:
        for j in range(3,i//2+1):
            if i%j==0:
                break
        else:
            res+=i
            c+=1
print(format(res/c,'.2f'))