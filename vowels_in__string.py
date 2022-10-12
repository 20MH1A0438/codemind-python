n=input()
l=[]
for ch in n:
    if (ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u') and (ch not in l):
     l.append(ch)
for i in l:
    print(i,end=' ')