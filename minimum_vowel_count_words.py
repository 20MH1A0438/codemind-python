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
co=min(list(dic.values()))
res=0
for v in dic.values():
    if v==co:
        res+=1
print(res)
        