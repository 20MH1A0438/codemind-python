n=input()
n=n.lower()
d=n.split(' ')
c=0
for i in d:
    for j in i:
        if j.isalpha():
            #print(j)
            pass
        else:
            c+=1
print(c)