def uniq(n):
    dig=str(n)
    uniq_dig=set(dig)
    return len(dig)==len(uniq_dig)
num=int(input())
if uniq(num):
    print("Unique Number")
else:
    print("Not Unique Number")