n=int(input())
l=list(map(int,input().split()))
c=0
k=0
for i in range(len(l)):
    if l[i]==0 or l[i]%2==0:
        c+=1
        if i%2==0 or i==0:
            k+=1
        else:
            p=1
            print(False)
            break
if c==k:
    print(True)
elif p!=1:
    print(False)