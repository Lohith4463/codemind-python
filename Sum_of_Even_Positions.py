n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    if i%2==0:
        a.append(l[i])
print(sum(a))