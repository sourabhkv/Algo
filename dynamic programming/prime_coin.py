from math import sqrt,ceil
n = int(input("enter n:"))
prime =[]
for i in range(2,n+1):
    flag = 0
    for j in range(2,i//2 + 1):
        if i % j ==0:
            flag = 1
            break
    
    if flag == 0:
        prime.append(i)

s = {}

for i in range(n+1):
    if i in prime:
        s[i] = [[i]]
    else:
        s[i] = []

for i in range(2,len(s)):
    current = s[i]
    for j in range(2,i-1):
        x = s[j]
        y = s[i-j]

        current.append(x[0] + y[0])
    
for i in s:
    input_lists = s[i]
    unique_lists = set(tuple(sorted(sub_list)) for sub_list in input_lists)
    unique_lists = [list(sub_list) for sub_list in unique_lists]
    s[i] = unique_lists

print(s[n])