n=input()
n=n.lower()
d=n.split(' ')
c=0
for i in d:
    c+=len(i)
print(c)