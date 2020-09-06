
/*
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
*/






import java.util.Arrays;
import java.util.List;

public class Problem_00 {
    public static boolean verify(List<Integer> list,int number){

        boolean verified = false ;
        for (int i=0 ; i< list.size();i ++ ){
            for (int j=0;j<list.size();j++){
                if (list.get(i) + list.get(j)  == number) {
                    verified=true ;
                }
            }
        }
        return verified ;
    }

public static void main(String[] args){
        List<Integer> list = Arrays.asList(10, 15, 7, 5);
        int number = 17 ;
        System.out.println(verify(list,number));
}

}


