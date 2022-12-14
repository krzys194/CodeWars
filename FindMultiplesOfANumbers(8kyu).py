# Link do zadania
# https://www.codewars.com/kata/58ca658cc0d6401f2700045f

def find_multiples(integer, limit):
    a = []
    b = 0
    while b <= limit:
        b += integer
        if b > limit:
            return a
        a.append(b)
    return a

find_multiples(5, 25)