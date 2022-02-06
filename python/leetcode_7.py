
def get_last_digit(num):
    if num <= 9:
        return num
    else:
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
    for i,v in enumerate(list_of_digits[::-1]):
        reverse += v*pow(10,i)
    if (reverse >= pow(-2,31) and reverse <= pow(2,31)-1 ):
        if x == 0:
            return reverse
        else:
            return (x//(abs(x)))*reverse
    else:
        return 0
            

if __name__ == '__main__':
    print(reverse(214748364))