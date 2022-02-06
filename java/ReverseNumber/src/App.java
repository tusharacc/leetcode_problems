import java.util.ArrayList;

public class App {

    public int reverse(int x) {
        int num = Math.abs(x);
        ArrayList<Integer> digits = new ArrayList<Integer>();

        while (true){
            digits.add(num%10);
            num = num / 10;

            if (num == 0){
                break;
            }
        }

        int lengthOfInteger = digits.size()-1;
        int reverseInteger = 0;

        for(int digit: digits){
            reverseInteger += digit*Math.pow(10, lengthOfInteger);
            lengthOfInteger--;
        }
        if (reverseInteger >= -2147483648 && reverseInteger < 2147483647 ){
            if (x == 0){
                return reverseInteger;
            }else{
                return (x/(Math.abs(x)))*reverseInteger;
            }
            
        } else {
            return 0;
        }
    }

    public static void main(String[] args) throws Exception {
        App app = new App();
        System.out.println(app.reverse(123));
    }
}
