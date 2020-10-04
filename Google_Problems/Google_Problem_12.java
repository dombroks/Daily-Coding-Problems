/*
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Google_Problem_12 {
    public static char[] segregateArray(char[] arr) {
        List<Integer> tempList = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            switch (arr[i]) {
                case 'R':
                    tempList.add(0);
                    break;
                case 'G':
                    tempList.add(1);
                    break;
                case 'B':
                    tempList.add(2);
                    break;
            }
        }
        Collections.sort(tempList);
        for (int i = 0; i < tempList.size(); i++) {
            switch (tempList.get(i)) {
                case 0:
                    arr[i] = 'R';
                    break;
                case 1:
                    arr[i] = 'G';
                    break;
                case 2:
                    arr[i] = 'B';
                    break;
            }
        }
        return arr;
    }

    public static void main(String[] args) {
        char[] array = {'G', 'B', 'R', 'R', 'B', 'R', 'G'};
        System.out.println(segregateArray(array));

    }
}
