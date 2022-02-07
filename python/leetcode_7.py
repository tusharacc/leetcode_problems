
def reverse( x: int) -> int:
    if x <= -2147483648 or x == 0:
        return 0
    num = abs(x)
    reverse_integer = 0
    
    while True:
        digit = num%10
        print ("reverse", reverse_integer, "digit", digit)
        reverse_integer = reverse_integer*10 + digit
        num = num // 10
        if num == 0:
            break

    if (reverse_integer <= 2147483647) :
        return (x//(abs(x)))*reverse_integer
    else:
        return 0
            

if __name__ == '__main__':
    print(reverse(123))
    #print(reverse(123))