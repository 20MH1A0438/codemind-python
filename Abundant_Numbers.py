n=int(input())
k=1
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        k+=i
        k+=(n//i)
if k>n:
    print(True)
else:
    print(False)
        
