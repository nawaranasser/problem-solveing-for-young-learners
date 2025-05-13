# n C r = n! / (n-r)!* r!

from math import factorial
def nCr(n , r):
    if r > n :
        return 0
    if r == 0:
        return 1
    denominator = factorial(r) * factorial(n-r)
    num_of_ways = factorial(n) // denominator

    return num_of_ways


print(nCr(n=2, r=4))