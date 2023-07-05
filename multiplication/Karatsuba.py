def karatsuba(x : int,y : int):
    if x<10 or y<10:
        return x*y
    
    n = max(len(str(x)),len(str(y)))
    n2 = n//2
    if n % 2!=0:
        n2+=1
    
    a = x // 10**n2
    b = x % 10**n2
    c = y // 10**n2
    d = y % 10**n2

    t1 = karatsuba(a,c)
    t2 = karatsuba(b,d)
    t3 = karatsuba(a+b,c+d) - t1 - t2

    return t1*10**(2*n2) + t3*10**(n2) +t2

num1 , num2 = 123456789101112131415,151413121110987654321
print(karatsuba(num1,num2))