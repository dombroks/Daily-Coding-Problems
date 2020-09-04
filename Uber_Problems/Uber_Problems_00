/*
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
*/



public class Problem_00 {
    public static int[] productArray(int[] array) {
        int [] array1 = new int[array.length] ;
        int s = 1 ;
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length; j++) {
                if (!(i == j)) {
                    int number = 1 * array[j];
                    s *= number;
                }
            }
            array1[i]=s ;
            s=1 ;
        }
        return array1;
    }

    public static void main(String[] args) {
        int [] array = {1, 2, 3, 4, 5} ;
        int [] array1 = productArray(array) ;
        for (int i = 0 ; i<array.length ; i++){
            System.out.println(array1[i]);
        }
    }
}


