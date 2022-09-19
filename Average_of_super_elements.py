n=int(input())
l=list(map(int,input().split()))
dic={}
for i in l:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
c=0
res=0
for k,v in dic.items():
    if k==v:
        c+=1
        res+=k
if c!=0:
    print(format(res/c,'.2f'))
else:
    print(-1)