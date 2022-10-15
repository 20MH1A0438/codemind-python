s1=input()
s2=input()
s1=s1.lower()
s1=s1.replace(" ","")
s2=s2.lower()
s2=s2.replace(" ","")
dic={}
s=''
for i in s1:
    if i not in dic:
        dic[i]=1
for j in s2:
    if j not in dic and j not in s:
        s+=j
    elif j not in dic and j in s:
        pass
    else:
        dic[j]+=1
for k,v in dic.items():
    if v==1:
        s+=k
print(len(s))