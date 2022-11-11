from math import sqrt


def pythagoras(a, b, c):
    if a == 0:
        return round(sqrt(b**2 + c**2), 2)
    elif b == 0:
        return round(sqrt(a**2 - c**2), 2)
    elif c == 0:
        return round(sqrt(a**2 + b**2), 2)
    else:
        return None

def simple_intrest(p, r, t):
    return (p*r*t)/100


#HELPER FUNCTION
def to_number(b):
    """
    This function takes in a string or list,
    converts the values into int and returns a list containing the numbers,
    If the input cannot be converted to int it returns an error message.
    
    """
    l = []
    for i in b:
        l.append(int(i))
    #for i in b:
    #     try:
    #         l.append(int(i))
    #     except ValueError:
    #         return "Invalid character."
    return l

# def area_of_sqr(s):
#     return s**2

# def area_of_rect(l, b):
#     return 2*(l + b)

# def area_of_tri(b, h):
#     return 0.5*b*h

# def area_of_circle(r):
#     pi = 3.142
#     return pi * (r**2)

# def area_of_sect(o, r):
#     return o/360 * area_of_circle(r)

# def area_of_trap(a, b, h):
#     return 0.5 * (a + b)*h

# def area_of_parallelogram(b, h):
#     return b * h

print(quadratic(5, 6, 3))
#sqr = sqrt(8) 

#print(sqr)

