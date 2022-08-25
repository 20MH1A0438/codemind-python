t=int(input())
l=list(map(int,input().split()))
l.sort()
a=sum(l)//len(l)
mid=t//2
l1=0
r=t
while t>1:
    if a==l[mid]:
        print(True)
        break
    elif a>l[mid]:
        l1=mid
        mid=(l1+r)//2
    else:
        r=mid
        mid=(l1+r)//2
    if mid==l1 or mid==r:
        print(False)
        break