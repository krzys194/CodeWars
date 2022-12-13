def phone_words(string_of_nums):
    buttons = { 
    0: " ", 2: "a", 22: "b", 222: "c", 3: "d", 33: "e", 333: "f", 4: "g",44: "h", 
    444: "i", 5: "j", 55: "k", 555: "l", 6: "m", 66: "n", 666: "o", 7: "p",
    77: "q", 777: "r", 7777: "s", 8: "t", 88: "u", 888: "v", 9: "w", 99: "x", 999: "y", 9999: "z",
    }
    i=0
    nrToStr = ""
    string_of_nums = string_of_nums+"-"
    newStr = string_of_nums[i]
       
    while string_of_nums[i] != "-":
        if newStr == "1":
            newStr = string_of_nums[i+1]
        elif newStr == "7777" or newStr == "9999":
            nrToStr += buttons[int(newStr)]
            newStr = string_of_nums[i+1]
        elif newStr == "777":
            if string_of_nums[i+1] == "7":
                newStr += string_of_nums[i+1]
            else:
                nrToStr += buttons[int(newStr)]
                newStr = string_of_nums[i+1]
        elif newStr == "999":
            if string_of_nums[i+1] == "9":
                newStr += string_of_nums[i+1]
            else:
                nrToStr += buttons[int(newStr)]
                newStr = string_of_nums[i+1]
        elif len(newStr) == 3:
            nrToStr += buttons[int(newStr)]
            newStr = string_of_nums[i+1]
        elif newStr == "0":
            nrToStr = nrToStr + " "
            newStr = string_of_nums[i+1]
        elif string_of_nums[i] == string_of_nums[i+1]:
            newStr += string_of_nums[i+1]
        else:
            nrToStr += buttons[int(newStr)]
            newStr = string_of_nums[i+1]
        i += 1
    return nrToStr