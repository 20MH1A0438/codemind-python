n=input()
s=n.split(' ')
m=''
for i in s:
    m+=min(i)
    m+=max(i)
mini=min(m)
maxi=max(m)
print(mini,n.count(mini),maxi,n.count(maxi))