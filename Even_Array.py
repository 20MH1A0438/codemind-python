n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i%2 and i!=0:
        print(False)
        break
else:
    print(True)