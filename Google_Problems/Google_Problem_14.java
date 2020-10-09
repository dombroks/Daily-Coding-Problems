/*
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
 */

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Google_Problem_14 {

    public static int get_non_duplicated_element(List<Integer> listOfNumbers) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : listOfNumbers) {
            if (map.containsKey(num)) {
                int value = map.get(num);
                map.replace(num, value + 1);
            } else map.put(num, 1);
        }

        return (int) map.keySet().toArray()[0];
    }

    public static void main(String[] args) {
        List<Integer> listOfNumbers = Arrays.asList(6, 1, 3, 3, 3, 6, 6);
        System.out.println(get_non_duplicated_element(listOfNumbers));
        //output : 1

        List<Integer> listOfNumbers2 = Arrays.asList(13, 19, 13, 13);
        System.out.println(get_non_duplicated_element(listOfNumbers2));
        //output : 19


    }
}
