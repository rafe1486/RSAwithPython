def pow_mod(a, b, c):
    "Calculate (x ** y) % z efficiently."
    number = 1
    count = 1
    while b:
        if b & 1:
            number = number * a % c
        b >>= 1
        a = a * a % c
    return number
'''        print("-- Round -- ",count," --")
        print("a = ",a)
        print("b = ",b)
        print("c = ",c)
        count+=1'''
    

#print (pow_mod(9,87654,321))