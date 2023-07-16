def partition( x: list):
    if len(x) > 1:
        left = 0
        right = len(x)
        pivot = x[left]
        i = left + 1
        for j in range(i, right):
            if x[j] < pivot:
                x[j] , x[i] = x[i] , x[j]
                i += 1
        
        x[left] , x[i-1] = x[i-1] , x[left]
        partition(x[:i])
        partition(x[i:])

n = [1,2,-1,3,0]
partition(n)
print(n)