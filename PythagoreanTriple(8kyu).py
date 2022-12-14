# Link do zadania
# https://www.codewars.com/kata/5951d30ce99cf2467e000013

def pythagorean_triple(integers):
    a = (integers[0])**2
    b = (integers[1])**2
    c = (integers[2])**2
    
    
    if a == b + c or b == a + c or c == b + a:
        return True
    else:
        return 0

pythagorean_triple([100,3,999])