def selection(x: list):
    for i in range(len(x)):
        m = i
        for j in range(i+1,len(x)):
            if x[m] > x[j]:
                m = j
        
        x[i] , x[m] = x[m] , x[i]

n = [4,1,2,-2,5]
selection(n)
print(n)