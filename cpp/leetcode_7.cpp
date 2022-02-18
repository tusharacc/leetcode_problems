//Some Comment

#include <iostream>
#include <cmath>

int reverse(int x){
    //std::vector<int> digits = {};
    
    int reverse = 0;
    int num = std::abs(x);
    int size = trunc(log10(num)) ;
    
    std::cout << "The number of digits" << size << std::endl;

    if (x <= -2147483648){
        return 0;
    }

    while (true){
    
        int digit = num%10;

        if (size > 9 && digit >= 3){
            return 0;
        } else if (reverse > 2147483600 && digit >= 5){
            return 0;
        }
        reverse = reverse + digit*pow(10,size);
        size--;
        num = num /10;
        
        
        if (num == 0){
            break;
        }
    }

    std::cout << "The number" << reverse << std::endl;

    //if (reverse >= -2147483648 and reverse <= 2147483647 ){
    if (x == 0){
        return 0;
    } else if (reverse < 0 && x > 0){
        return 0;
    }
    else{
        return (x/(abs(x)))*reverse;
    }
        
        
}

int main(int argc,char *argv[]){
    //std::cout << reverse(-2147483648);
    std::cout << reverse(1563847412) << std::endl;
    std::cout << reverse(123456) << std::endl;
    std::cout << reverse(1534236469) << std::endl;
    std::cout << reverse(1563847412) << std::endl;
}

//-2147483648
// 2147483648
// 2147483651