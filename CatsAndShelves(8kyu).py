# Link do zadania
# https://www.codewars.com/kata/62c93765cef6f10030dfa92b

def solution(start, finish):
    steps = -1
    sC = finish-start
    if 0<=sC<=2:
        return sC
    sum = sC/3
    if (sum) == int(sum):
        return int(sum)
    elif sum<(int(sum))+0.5:
        return int(sum)+1
    else:
        return int(sum)+2

solution(1,5)