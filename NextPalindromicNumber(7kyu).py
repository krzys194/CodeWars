# Link do zadania
# https://www.codewars.com/kata/56a6ce697c05fb4667000029

def next_pal(val):
    a = True
    while a:
        rev=0
        val += 1
        temp=val
        aCopyVal = val
        while(aCopyVal>0):
            dig=aCopyVal%10
            rev=(rev*10)+dig
            aCopyVal=aCopyVal//10
        if(temp==rev):
            a = False
            return rev
        
next_pal(11)