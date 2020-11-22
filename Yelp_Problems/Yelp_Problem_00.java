/*
This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
 */

import java.util.*;

public class Yelp_Problem_00 {
    public static List<String> letterCombination(Map<Integer, List<String>> map, String digit) {
        List<String> combination = new ArrayList<>();
        int[] arr = new int[digit.length()];
        for (int i = 0; i < digit.length(); i++) {
            arr[i] = Integer.parseInt(String.valueOf(digit.charAt(i)));
        }
        if (arr.length == 1) {
            return map.get(arr[0]);
        } else if (arr.length == 2) {
            combination.addAll(combineStrings(map.get(arr[0]), map.get(arr[1])));
            return combination;
        }
        combination.addAll(map.get(arr[0]));
        for (int i = 1; i < arr.length - 1; i++) {
            List<String> tempList = combineStrings(map.get(arr[i]), map.get(arr[i + 1]));
            combination = combineStrings(combination, tempList);
        }
        return combination;
    }

    public static List<String> combineStrings(List<String> list1, List<String> list2) {
        List<String> combination = new ArrayList<>();
        for (int i = 0; i < list1.size(); i++) {
            for (int j = 0; j < list2.size(); j++) {
                combination.add(list1.get(i) + list2.get(j));
            }
        }
        return combination;
    }

    public static void main(String[] args) {
        Map<Integer, List<String>> map = new HashMap();
        map.put(2, Arrays.asList("a", "b", "c"));
        map.put(3, Arrays.asList("d", "e", "f"));
        System.out.println(letterCombination(map, "23"));
    }
}
