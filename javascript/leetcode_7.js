/**
 * @param {number} x
 * @return {number}
 */

var last_digit = function(num){
    return num%10;
}
var reverse = function(x) {
    num = Math.abs(x);
    list_of_digits = [];
    while (true){
        list_of_digits.push(last_digit(num));
        num = Math.floor(num/10);
        if (num == 0){
            break
        }
    }

    console.log(list_of_digits)
    length_of_integer = list_of_digits.length - 1
    reverse_number = 0
    list_of_digits.forEach(e =>{
        reverse_number += e*Math.pow(10,length_of_integer)
        length_of_integer -= 1
    })
    console.log("The number", reverse_number)
    if (reverse_number >= Math.pow(-2,31) && reverse_number <= Math.pow(2,31)-1 ){
        if (x == 0){
            return reverse_number
        }    
        else{
            return (x/(Math.abs(x)))*reverse_number
        }
            
    }else{
                
        return 0;        
    }
        
};

console.log(reverse(123));