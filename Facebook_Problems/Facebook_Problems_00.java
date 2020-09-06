


public class Facebook_Problems_00 {
    public static int productArray(String message) {
        int counter = 1 ;
        for (int i = 0; i<message.length()-1;i ++ ){
            int firstNumber =Integer.parseInt(String.valueOf(message.charAt(i))) ;
            int secondNumber =Integer.parseInt(String.valueOf(message.charAt(i+1))) ;
            if ((firstNumber * 10 + secondNumber) < 27){
                counter ++ ;
            }
        }
        return counter ;

    }



    public static void main(String[] args) {

        System.out.println(productArray("111"));

    }
}

