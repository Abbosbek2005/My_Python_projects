import math
#Biquadratic equation solutions: A*x^4+B*x^2+C=0
"""This function find solutions of biquadratic(pow of x == 4) equation 
using discriminat formula and gives its existing(real) solutions
"""

#Find discriminant of the equation first
def function(a,b,c):
    d=b**2-4*a*c

#If discriminant is positive find the two solutions
#Then, calculate square roots of positive ones 
    if d>0:
        x1=(-b+math.sqrt(d))/(2*a)
        if x1>0:
            x1=math.sqrt(x1)
            print(f"Yes, +{x1} and -{x1}")

        else:
            print(" no X1")
        x2=(-b-math.sqrt(d))/(2*a)
        if x2>0:
            x=math.sqrt(x2)
            print(f"Yes, +{x2} and -{x2}")
        else:
            print(" no X2")

#If discriminant is zero , just find the one solution
#And, calculate square root of it    
    elif d==0:
        x=-b/(2*a)
        if x>0:
            x=math.sqrt(x)
            print(x)
            
#All the cases above do notwork means that there are no 
#real solutions of this equation
    else:
        print("No solution")
print(function(1,2,-3))
