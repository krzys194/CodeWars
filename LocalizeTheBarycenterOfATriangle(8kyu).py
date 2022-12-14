# Link do zadania
# https://www.codewars.com/kata/5601c5f6ba804403c7000004


def bar_triang(point_a, point_b, point_c): 
    Xo = round((point_a[0] + point_b[0] + point_c[0])/3,4)
    Yo = round((point_a[1] + point_b[1] + point_c[1])/3,4)
    return[Xo, Yo]

bar_triang([4, 6], [12, 4], [10, 10])