from math import ceil , sqrt

def primeproduct(n : int, x : list = []):
    if n > 1:
        if len(x)>=1 and x[-1] % n == 0:
            x.append(x[-1])
            n = n // x[-1]
        
        else:
            sq = ceil(sqrt(n))
            flag = 0
        
            for i in range(2 , sq+1):
                if n % i == 0:
                    n = n // i
                    x.append(i)
                    flag = 1
                    break
                
            if not flag:
                x.append(n)
                n = 1
            
        return primeproduct(n,x)
    
    return x

n = int( input ("enter n: ") )
print( primeproduct(n) )