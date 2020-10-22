s = input()
a, b = s.split()
a = int(a)
b = int(b)
def gcd(a,b):
    if a < b:
        a,b = b,a
    return a if b==0 else gcd(b, a%b)
print(gcd(a,b))