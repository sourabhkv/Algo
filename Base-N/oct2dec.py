def oct2dec(n: str):
    if len(n)==1:
        return int(n)
    
    return int(n[0]) * 8**(len(n)-1) + oct2dec(n[1:])

print(oct2dec("775"))