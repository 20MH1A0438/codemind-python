n=input()
d=n.split(' ')
m='aeiouAEIOU'
c=0
for i in d:
    if (i[0] in m) and (i[-1] not in m):
        c+=1
print(c)
        