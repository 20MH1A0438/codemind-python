n=int(input())
temp=n
while n>0:
    n-=1
    k=str(n)
    if k==k[::-1]:
        y=abs(temp-n)
        break
n=temp
while n>0:
    n+=1
    h=str(n)
    if h==h[::-1]:
        u=abs(temp-n)
        break
if y==u:
    print(k,h)
elif y>u:
    print(h)
else:
    print(k)
