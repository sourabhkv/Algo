def dec2oct( n : int):
    if n <= 7:
        return str(n)
    
    return dec2oct(n//8) + str(n%8)

print(dec2oct(217))