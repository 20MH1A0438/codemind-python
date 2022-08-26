def prime(n,m):
    k=0
    for i in range(n,m):
        if i%2:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    break
            else:
                k+=1
    return k
n=int(input())
m=int(input())
m+=1
print(prime(n,m))
