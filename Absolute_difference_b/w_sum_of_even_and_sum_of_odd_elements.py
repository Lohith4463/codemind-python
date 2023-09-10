n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
c=sum(a)
d=sum(b)
print(abs(c-d))