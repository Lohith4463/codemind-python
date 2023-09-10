def adam(n):
    s=0
    while(n):
        s=s*10+(n%10)
        n//=10
    return s
n=int(input())
r=adam(n)
s=n*n
a=r*r
k=adam(s)
if(k==a and n==adam(r)):
    print(True)
else:
    print(False)