# link do zadania:
# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python

def human_years_cat_years_dog_years(human_years):
    c, d = 0, 0
    for i in range(0, human_years):
        if i == 0:
            c = 15
            d = 15
        elif i == 1:
            c += 9 
            d += 9
        else:
            c += 4
            d += 5
    return [human_years, c, d]

    human_years_cat_years_dog_years(10)