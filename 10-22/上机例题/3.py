from math import sqrt
s = int(input())
def is_prime(a):
    if a == 1:
        return False
    if a == 2:
        return True
    for i in range(2,int(sqrt(a)) + 1):
        if s % i == 0:
            return False
    return True
    
print(is_prime(s))