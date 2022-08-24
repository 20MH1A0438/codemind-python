n=int(input())
n=str(n)
k=0
for i in range(0,len(n)):
    k+=int(n[i])**(i+1)
if int(n)==k:
    print(True)
else:
    print(False)