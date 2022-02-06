#include <iostream>
#include <vector>
#include <cmath>

int reverse(int x){
    std::vector<int> digits = {};

    if (x <= -2147483648){
        return 0;
    }

    int num = std::abs(x);

    std::cout << "The original number" << x << std::endl;

    while (true){
        std::cout << "the number is " << num << std::endl;
        digits.push_back(num%10);
        num = num /10;
        if (num == 0){
            break;
        }
    }
    //std::cout << digits;
    int reverse = 0;
    int lengthOfDigits = digits.size()-1;

    for (int i = 0; i < digits.size();i++){
            std::cout << "The digits are" << reverse << "----"<< digits[i]  << std::endl;
            if (lengthOfDigits >= 9 && digits[i] >= 3){
                return 0;
            } else if (reverse > 2147483600 && digits[i] >= 5 ) {
                return 0;
            }
            else {
                //std::cout << "The digits again " << digits[i] << lengthOfDigits << std::endl;
                reverse = reverse + digits[i]*(pow(10,lengthOfDigits));
                lengthOfDigits--;
            }
        }
        
        //std::cout << "The number" << reverse << std::endl;

        //if (reverse >= -2147483648 and reverse <= 2147483647 ){
        if (x == 0){
            return reverse;
        } else if (reverse < 0 && x > 0){
            return 0;
        }
        else{
            return (x/(abs(x)))*reverse;
        }
        
        
}

int main(int argc,char *argv[]){
    //std::cout << reverse(-2147483648);
    std::cout << reverse(1563847412);
}

//-2147483648
// 2147483648
// 2147483651