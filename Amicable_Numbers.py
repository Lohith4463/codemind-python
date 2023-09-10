def proper_div(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s

def amicable(n):
    sn = proper_div(n)
    ssn = proper_div(sn)
    return n == ssn and n != sn

n = int(input())

if amicable(n):
    print("Amicable")
else:
    print("Not Amicable")
