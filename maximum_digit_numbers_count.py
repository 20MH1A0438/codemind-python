n=input()
l=list(map(int,input().split()))
lis=[]
for i in l:
    lis.append(len(str(abs(i))))
maxi=max(lis)
for j in l:
    if len(str(abs(j)))==maxi:
        print(j,end=' ')
