n=input()
n=n.lower()
s=n.split()
vowels='aeiou'
c=0
for i in s:
    length=len(i)
    j=0
    while j<len(i)//2:
        if i[j] in vowels and i[-(j+1)] not in vowels:
            c+=1
        elif i[-(j+1)] in vowels and i[j] not in vowels:
            c+=1
        j+=1
print(c)