# Link do zadania
# https://www.codewars.com/kata/5a57d101cadebf03d40000b9/train/python

from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_leaderboard_honor():
    html = urlopen('https://www.codewars.com/users/leaderboard')
    bs = BeautifulSoup(html.read(), 'html.parser')
    B = bs.find_all(class_ = 'honor')
    C = []
    
    for nr, x in enumerate(B):
        a = [x.get_text().replace(",", '')]
        C += a
    A = [eval(i) for i in C]
    return A


