# link do zadania:
# https://www.codewars.com/users/Krzys194/completed_solutions

def hotpo(n):
    i = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
            i += 1
        else:
            n = 3 * n + 1
            i += 1
    return i

hotpo(23)