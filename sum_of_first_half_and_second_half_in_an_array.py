n=int(input())
l=list(map(int,input().split()))
f_c=0
s_c=0
for i in range(n):
    if i<n//2:
        f_c+=l[i]
    else:
        s_c+=l[i]
print(f_c)
print(s_c)