n=input()
d=n.split(' ')
c=0
for i in d:
    for j in i:
        if j.islower():
            c+=1
print(c)
