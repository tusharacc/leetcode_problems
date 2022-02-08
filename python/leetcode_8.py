from tkinter.tix import INTEGER


@profile
def myAtoi( s):
    s = s.lstrip()
    if len(s) == 0:
        return 0


    if s[0] == "-":
        negative,start = True,1
    elif s[0] == "+":
        negative,start = False,1
    else:
        negative,start = False,0

    number = 0

    for c in range(start,len(s)):
        code = ord(s[c])
        if code >= 48 and code <= 57:
            number = number*10 + (code - 48)
        else:
            break
        
        
    number = -1*number if negative else number

    number = -2147483648 if number < -2147483648 else number
    number = 2147483647 if number > 2147483647 else number

    return number

if __name__ == '__main__':
    print(myAtoi("12345678"))
    print(myAtoi("+345"))
    print(myAtoi("-12345678"))
    print(myAtoi("-394589512345678"))
    print(myAtoi("+12345678"))
    print(myAtoi("345678"))
    print(myAtoi("     345678"))
