def romanToInt(s):
    mapRomanToInt = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    sum = 0
    for index,character in enumerate(s[0:-1]):
        if mapRomanToInt[character] < mapRomanToInt[s[index+1]]:
            sum += ((-1)*mapRomanToInt[character])
        else:
            sum += mapRomanToInt[character]

    sum += mapRomanToInt[s[-1]]
    return sum

print (romanToInt('IV'))