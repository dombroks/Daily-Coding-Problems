/*
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
 */


public class Amazon_Problem_07 {
    public static int findElementHelper(int[] arr, int element, int start, int end) {

        if (start == end) return -1;
        int mid = start + ((end - start) / 2);
        if (arr[mid] == element) return mid;
        else if (arr[mid] > element) {
            if (arr[start] >= element) return findElementHelper(arr, element, start, mid);
            else return findElementHelper(arr, element, mid, end);
        } else if (arr[mid] < element) {
            if (arr[start] <= element) return findElementHelper(arr, element, start, mid);
            else return findElementHelper(arr, element, mid, end);
        }

        return -1;
    }

    public static int findElement(int[] arr, int element) {
        int elementPosition = findElementHelper(arr, element, 0, arr.length);
        return elementPosition;

    }


    public static void main(String[] args) {
        int [] arr = {13, 18, 25, 2, 8, 10} ;
        assert findElement(arr, 8) == 4 ;

    }
}
