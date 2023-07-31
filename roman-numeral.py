#Numeric to Roman Numeral Converter
number = int(input("\nEnter a number: "))
romanNumeral = {
    1:"I", 4:"IV", 5:"V", 
    9:"IX", 10:"X", 20:"XX", 30:"XXX",
    40:"XL", 50:"L", 60:"LX" , 70:"LXX", 80:"LXXX", 
    90:"XC", 100:"C", 200:"CC", 300:"CCC",
    400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 
    900:"CM", 1_000:"M"
    }

def convert(num):
    str_num = str(num)
    roman = ""
    if len(str_num) == 1:
        roman += romanNumeral[int(digit) * root]
    elif len(str_num) == 2:
        root = 10
        for digit in str_num:
            roman += (romanNumeral[int(digit) * root])
            root //= 10
    elif len(str_num) == 3:
        root = 100
        for digit in str_num:
            roman += romanNumeral[int(digit) * root]
            root //= 10
    elif len(str_num) == 4:
        root = 1_000
        for digit in str_num:
            roman += romanNumeral[int(digit) * root]
            root //= 10
    else:
        return "Out of range"

    return roman
        
print(f"Roman Numeral of {number} is", convert(number))
