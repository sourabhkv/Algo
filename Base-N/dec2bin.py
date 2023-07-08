def dec2bin( n : int):
    if n <= 1:
        return str(n)
    
    return dec2bin(n//2) + str(n%2)

print(dec2bin(217))