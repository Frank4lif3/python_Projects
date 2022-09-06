#further research: Euclid's Algorithm
# if p > q, gcd of p and q  is same as gcd of q and p % q

def GCD(int1, int2):
    remainder = int1 % int2
    print(int1, int2, remainder)

GCD(20, 10)