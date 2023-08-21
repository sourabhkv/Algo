a=[1,2,3,5]
count = 11

def dp(count: int, x: int =[]):
    c = [0] * (count+1)
    for i in range(1,len(c)):
        if i in x:
            c[i] = 1
        
        else:
            temp = []
            for j in range(1,i):
                temp.append(c[j]+ c[i-j])
            
            if temp:
                c[i] = min(temp)
    
    for i in range(len(c)):
        print("value ",i,"=",c[i])

dp(count,a)