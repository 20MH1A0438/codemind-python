n=input()
n=n.lower()
s='aeiou'
m=''
c=0
for i in n:
    if i in s:
        m+=i
for i in s:
    if i not in m:
        c=1
        print(i,end=' ')
if c==0:
    print(0)
