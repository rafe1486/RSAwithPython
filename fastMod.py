def pow_mod(a, b, c):
    "Calculate (a ** b) % c"
    result = 1
    while b:
        if b & 1:
            result = result * a % c
        b >>= 1
        a = a * a % c
    return result

    
#print(pow_mod(9,87654,321))