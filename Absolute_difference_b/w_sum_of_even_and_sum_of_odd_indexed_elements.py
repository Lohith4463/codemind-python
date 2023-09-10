n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(n):
    if i%2==0:
        a.append(l[i])
    else:
        b.append(l[i])
c=sum(a)
d=sum(b)
print(abs(c-d))