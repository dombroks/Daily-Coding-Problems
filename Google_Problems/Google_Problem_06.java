/*
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
 */
public class Google_Problem_06 {

    public static void subarrayMaximum(int[] array, int k) {
        int[] temp = new int[k];
        for (int i = 0; i < array.length - k + 1; i++) {
            for (int j = 0; j < k; j++) {
                temp[j] = array[j + i];
            }
            System.out.println(max(temp));
        }
    }

    private static int max(int[] array) {
        int max = 0;
        for (int i = 0; i < array.length; i++) {
            if (array[i] > max) max = array[i];
        }
        return max;
    }

    public static void main(String[] args) {
        int[] arr = {10, 5, 2, 7, 8, 7};
        int k = 3;
        subarrayMaximum(arr, k);
    }
}
