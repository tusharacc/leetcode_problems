import math

def isPalindrome( x: int) -> bool:
    if x < 0:
        return False
    
    reverse_integer = 0
    num = x
    while True:
        digit = num%10    
        reverse_integer = reverse_integer*10 + digit
        num = num// 10
        if num == 0:
            break
            
    print (reverse_integer)
    if x == reverse_integer:
        return True
    
    return False
    
if __name__ == '__main__':
    #print (isPalindrome(313))
    print (isPalindrome(1000021))
