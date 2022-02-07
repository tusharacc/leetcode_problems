/**
 * @param {number} x
 * @return {number}
 */


var reverse = function(x) {

    if (x <= -2147483648 || x == 0){
        return 0;
    }

    num = Math.abs(x);
    let reverseInteger = 0;

    while (true){
        let digit = num%10;
        reverseInteger = reverseInteger*10 + digit;
        num = Math.floor(num/10);
        if (num == 0){
            break
        }
    }

    if (reverseInteger <= 2147483647 ){
        return (x/(Math.abs(x)))*reverseInteger
    }else{
        return 0;        
    }
        
};

console.log(reverse(123));
console.log(reverse(1563847412));