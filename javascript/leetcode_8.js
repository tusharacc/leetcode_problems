var myAtoi = function(s) {
    s = s.trim();

    let number = 0;

    let negative = s[0] === "-"? true : false
    let start = s[0] === "-" || s[0] === "+" ? 1 : 0

    for (let i = start; i < s.length; i++){
        let code = s.charCodeAt(i);
        if ( code >= 48 &&  code <= 57){
            number = number*10 + (code-48)
        //if (s[i] in ['0','1','2','3','4','5','6','7','8','9']){
        //    number = number*10 + parseInt(s[i]);
        } else {
            break;
        }
    }

    number  = negative ? -1*number : number; 
    number = number < -2147483648 ? -2147483648 : number;
    number = number > 2147483647 ? 2147483647 : number;

    
    return number;
};
    

let val = myAtoi("123")
console.log(val, typeof val);
val = myAtoi("-123")
console.log(val, typeof val);
val = myAtoi("+123")
console.log(val, typeof val);
val = myAtoi("0")
console.log(val, typeof val);
val = myAtoi("-91283472332")
console.log(val, typeof val);
//console.log(myAtoi("+123"));
//console.log(myAtoi("-1233   "));