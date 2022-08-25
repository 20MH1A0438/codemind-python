t=int(input())
a=list(map(int,input().split()))
o=0
e=0
for i in a:
    if i%2:
        o+=i
    else:
        e+=i
print(abs(o-e))