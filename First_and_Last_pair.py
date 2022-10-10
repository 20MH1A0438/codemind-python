n=int(input())
l=list(map(int,input().split()))
i=0
j=n-1
while i<=n//2:
    if i!=j and i<j:
        print(l[i],l[j],end=' ')
        i+=1
        j-=1
    elif i>j:
        break
    else:
        print(l[i],0)
        break