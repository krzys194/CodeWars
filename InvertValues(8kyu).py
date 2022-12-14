# Link do zadania
# https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad

def invert(lst):
    newLst = []
    for i in range(0,len(lst)):
        newLst.append(int(lst[i]*(-1)))
    return(newLst)

invert([1,2,3,4,5])