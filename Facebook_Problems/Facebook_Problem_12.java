/*
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
 */

import java.util.Arrays;
import java.util.List;

public class Facebook_Problem_12 {
    public static int getLargestProduct(List<Integer> list) {
        int product = 0;
        for (int i = 0; i < list.size(); i++) {
            for (int j = i; j < list.size(); j++) {
                for (int k = j; k < list.size(); k++) {
                    int s = list.get(i) * list.get(j) * list.get(k);
                    product = Math.max(product, s);
                }
            }
        }
        return product;
    }

    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(-10, -10, 5, 2);
        System.out.println(getLargestProduct(list));// Output : 500
    }
}
