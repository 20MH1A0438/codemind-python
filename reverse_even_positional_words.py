n=input()
d=n.split(' ')
for i in d:
    if d.index(i)==0:
        print(i[::-1],end=' ')
    elif d.index(i)%2==0:
        print(i[::-1],end=' ')
    else:
        print(i,end=' ')
        

    