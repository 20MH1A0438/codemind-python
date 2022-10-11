n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1=set(l1)
l2=set(l2)
dic={}
for i in l1:
    dic[i]=1
for i in l2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
res=0
for v in dic.values():
    if v==1:
        res+=1
print(res)
    