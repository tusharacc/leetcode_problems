
@profile
def reverse( x: int) -> int:
    num = abs(x)
    list_of_digits = []
    reverse_string = ''
    while True:
        #q,rem = divmod(num,10)
        digit = num%10
        reverse_string += digit
        num = num // 10
        if num == 0:
            break
    reverse_integer = int(reverse_string)
    if (reverse_integer >= -2147483648 and reverse_integer <= 2147483647 ):
        if x == 0:
            return reverse
        else:
            return (x//(abs(x)))*reverse_integer
    else:
        return 0
            

if __name__ == '__main__':
    print(reverse(214748364))