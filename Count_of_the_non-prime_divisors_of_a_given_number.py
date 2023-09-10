n=int(input())
a=[]
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
d=0
for i in a:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c!=2:
        d+=1
print(d)
