import math
def find_roots(a,b,c):
    d=b*b-4*a*c
    if(d==0):
        return (-b/(2*a),-b/(2*a))
    elif(d>0):
        return ((-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a))
    else:
        return (str(-b/(2*a))+"+i"+str(math.sqrt(-d)/(2*a)),str(-b/(2*a))+"-i"+str(math.sqrt(-d)/(2*a)))
ans = find_roots(1,1,1)
print(ans)