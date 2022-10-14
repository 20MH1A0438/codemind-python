n=input()
s=n.split(' ')
max_c=0
min_c=0
for i in s:
    max_c+=ord(max(i))
    min_c+=ord(min(i))
    #print(i,max_c,min_c)
print(abs(max_c-min_c))
    
    