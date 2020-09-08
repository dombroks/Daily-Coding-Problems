/*

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

*/



public class Problem_00 {
    public static int getMissingPositiveInteger(int[] array) {
        int magicNumber = 1;
        while (checkExist(array, magicNumber)) {
            magicNumber++;
        }
        return magicNumber;
    }

    public static boolean checkExist(int[] array, int number) {
        boolean isExisted = false;
        for (int i = 0; i < array.length; i++) {
            if (array[i] == number) {
                isExisted = true;
            }
        }
        return isExisted;
    }

    public static void main(String[] args) {
        int[] array = {1, 2, 0};
        System.out.println(getMissingPositiveInteger(array));

    }
}


