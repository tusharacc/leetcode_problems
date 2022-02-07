from math import log
#@profile
def reverse( x: int) -> int:
    #if x <= -2147483648 or x == 0 or x > 2147483647 :
    #    return 0
    num = abs(x)
    length_of_integer = int(log(num,10))
    reverse_integer = 0
    while True:
        #q,rem = divmod(num,10)
        digit = num%10
        reverse_integer += digit*(10**length_of_integer)
        #print (reverse_integer,"dsfd")
        length_of_integer -= 1
        num = num // 10
        if num == 0:
            break
    #print (reverse_integer)
    #reverse_integer = int(reverse_string)
    if (reverse_integer >= -2147483648 and reverse_integer <= 2147483647 and reverse_integer != 0) :
        return (x//(abs(x)))*reverse_integer
    else:
        return 0
            

if __name__ == '__main__':
    print(reverse(214748364))
    #print(reverse(123))