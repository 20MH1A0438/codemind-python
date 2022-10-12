n=input()
s='aeiou'
c=0
m=''
for i in n:
    if i in s and i not in m:
        c+=1
        m+=i
if c==5:
    print(True)
else:
    print(False)