n=int(input())
l=n*n
n=str(n)
n=n[::-1]
k=int(n)*int(n)
k=str(k)
k=k[::-1]
if l==int(k):
    print(True)
else:
    print(False)