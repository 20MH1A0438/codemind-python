n=input()
n=n.lower()
d=n.split(' ')
m='aeiou'
for i in d:
    c=0
    for j in i:
        if j in m:
            c+=1
    print(c,end=' ')