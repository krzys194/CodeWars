# Link do zadania
# https://www.codewars.com/kata/609eee71109f860006c377d1

def last_survivor(letters, coords): 
    n = list((" ".join(letters)).split(" "))
    for i in range(0, len(coords)):
        del n[coords[i]]
    return (" ".join(n))

last_survivor('abc', [1, 1])