n=input()
n=n.lower()
d=n.split(' ')
m='aeiou'
dic={}
for i in d:
    c=0
    for j in i:
        if j in m:
            c+=1
    dic[i]=c
co=max(list(dic.values()))
print(co)
        