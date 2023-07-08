def bintodec(n: str):
    if len(n)==1:
        return int(n)
    
    return int(n[0]) * 2**(len(n)-1) + bintodec(n[1:])

print(bintodec("1011"))