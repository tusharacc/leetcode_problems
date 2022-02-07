

public class App {

    public int reverse(int x) {

        if (x <= -2147483648 || x == 0){
            return 0;
        }

        long reverseInteger = 0;

        int num = Math.abs(x);
        int digit = 0;
        
        //ArrayList<Integer> digits = new ArrayList<Integer>();

        while (true){
            //digits.add(num%10);
            digit = num % 10;
            num = num / 10;
            System.out.println("The revreseing is "+ reverseInteger+ " .The digit is"+digit);
            reverseInteger = reverseInteger*10 + digit;

            if (num == 0){
                break;
            }
        }


        //System.out.println("The compare value is "+ reverseString.compareTo("2147483647"));
        //if (reverseString.compareTo("2147483647") < 0){
        //    return 0;
        //}
       
        if (reverseInteger <= -2147483648 || reverseInteger > Integer.MAX_VALUE){
            return 0;
        } else {
            return (x/Math.abs(x))*(int)reverseInteger;
        }

        //if (reverseInteger >= -2147483648 && reverseInteger < 2147483647 ){
            
        //} else {
        //    return 0;
        // }
    }

    public static void main(String[] args) throws Exception {
        App app = new App();
        //System.out.println(app.reverse(1563847412));
        //System.out.println(app.reverse(-123));
        System.out.println(app.reverse(1534236469));
        //System.out.println(app.reverse(1534236469));
        //System.out.println(app.reverse(0));
        //System.out.println(app.reverse(1563847412));
    }
}

//9646324350
//2147483647
//1534236469
