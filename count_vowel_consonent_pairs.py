n=input()
n=n.lower()
vowel='aeiou'
i=0
c=0
while i<len(n)//2:
    if (n[i] in vowel and n[-(i+1)] not in vowel) or (n[i] not in vowel and n[-(i+1)] in vowel):
        if n[i]!=' ' and n[-(i+1)]!=' ':
            c+=1
    i+=1
print(c)