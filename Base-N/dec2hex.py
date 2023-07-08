def maper(n: int):
    if n<=9:
        return str(n)
    
    s  = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    return s[n]

n = int(input("enter n : "))
result = ""
while n!=0:
    rem = n % 16
    qt  = n // 16
    result = maper(rem) + result
    n = qt

print(result)