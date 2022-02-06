
def get_last_digit(num):
    return num%10

@profile
def reverse( x: int) -> int:
    num = abs(x)
    list_of_digits = []
    while True:
        #q,rem = divmod(num,10)
        list_of_digits.append(get_last_digit(num))
        
        num = num // 10
        if num == 0:
            #list_of_digits.append(q)
            #reverse += q
            break
    reverse = 0

    length_of_integer = len(list_of_digits)-1
    reverse = 0
    for i in list_of_digits:
        reverse += i*pow(10,length_of_integer)
        length_of_integer -= 1
    if (reverse >= -2147483648 and reverse <= 2147483647 ):
        if x == 0:
            return reverse
        else:
            return (x//(abs(x)))*reverse
    else:
        return 0
            

if __name__ == '__main__':
    print(reverse(214748364))