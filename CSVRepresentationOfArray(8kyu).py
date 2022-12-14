# Link do zadania
# https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036

def to_csv_text(array):
        a = ''.join(str(array))
        a = a.replace("], [", "\n")
        a = a.replace("[", "")
        a = a.replace("]", "")
        a = a.replace(" ", "")
        return a


to_csv_text([
            [-25, 21, 2, -33, 48],
            [30, 31, -32, 33, -34]
        ])