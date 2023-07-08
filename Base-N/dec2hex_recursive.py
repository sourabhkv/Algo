def maper( n: int ):
    if n <= 9:
        return str(n)
    
    s  = { 10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F" }
    return s[n]

def dec2hex( x : int ):
    if x < 16:
        return maper( x )
    
    else:
        return dec2hex(x // 16) + maper(x % 16)

n = int( input ("enter n : "))
print( dec2hex( n ) )