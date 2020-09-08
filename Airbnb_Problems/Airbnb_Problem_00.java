/*
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
 */



import java.util.Arrays;
import java.util.List;

public class Airbnb_Problem_00 {
    public static int largestSum(List<Integer> list) {
        int size = list.size();
        int s = 0;
        for (int i = 0; i < list.size(); i++) {
            s = s + list.get(i);

        }
        if (size % 2 != 0) {
            s = s - list.get(size / 2);
        } else
            s = s - (list.get((size / 2) - 1) + list.get(size / 2));

        return s;
    }
    public static void main(String[] args) {
        List<Integer> data = Arrays.asList(2, 4, 6, 2, 5);
        System.out.println(largestSum(data));

    }
}


