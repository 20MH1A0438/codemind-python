n=input()
n=n.split(' ')
m=min(n[-1])
if m.islower():
    print(m)
elif m.isupper() and chr(ord(m)+32) not in n[-1]:
    print(m)
else:
    print(chr(ord(m)+32))