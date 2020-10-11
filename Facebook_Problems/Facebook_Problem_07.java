/*
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
 */

public class Facebook_Problem_07 {

    public static void get_remain_trapped_water_units(int[] arr) {
        int size = arr.length - 1;
        int prev = arr[0];
        int prev_index = 0;
        int water = 0;
        int temp = 0;
        for (int i = 1; i <= size; i++) {
            if (arr[i] >= prev) {
                prev = arr[i];
                prev_index = i;
                temp = 0;
            } else {
                water += prev - arr[i];
                temp += prev - arr[i];
            }
        }

        if (prev_index < size) {
            water -= temp;
            prev = arr[size];
            for (int i = size; i >= prev_index; i--) {
                if (arr[i] >= prev) {
                    prev = arr[i];
                } else {
                    water += prev - arr[i];
                }
            }
        }

        System.out.println(water);
    }

    public static void main(String[] args) {
        int[] arr = new int[]{3, 0, 1, 3, 0, 5};
        get_remain_trapped_water_units(arr);
    }
}
