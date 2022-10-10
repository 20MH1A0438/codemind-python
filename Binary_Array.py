n=int(input())
l=list(map(int,input().split()))
for i in l:
    if int(i)!=0 and int(i)!=1:
        print(False)
        break
else:
    print(True)