/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
*/

import java.util.Arrays;
import java.util.List;

public class Google_Problem_07 {
    public static int getIntersectionValue(List<Integer> l1, List<Integer> l2) {
        int temp = 0;
        for (int i = 0; i < l1.size(); i++) {
            temp = l1.get(i);
            if (l2.contains(temp)) {
                break;
            }
        }
        return temp;
    }

    public static void main(String[] args) {
        List<Integer> l1 = Arrays.asList(3, 7, 8, 10);
        List<Integer> l2 = Arrays.asList(99, 1, 8, 10);
        System.out.println(getIntersectionValue(l1, l2));
    }
}
