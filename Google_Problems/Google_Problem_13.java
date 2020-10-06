/*
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Google_Problem_13 {

    public static List<List<Integer>> get_power_set(List<Integer> listOfNumbers) {
        List<Integer> tempList;
        List<List<Integer>> finalLIst = new ArrayList<>();

        //Adding empty list
        finalLIst.add(Arrays.asList());

        for (int i = 0; i < listOfNumbers.size(); i++) {
            tempList = new ArrayList<>();
            int temp = listOfNumbers.get(i);
            tempList.add(temp);
            finalLIst.add(tempList);
        }

        for (int i = 0; i < listOfNumbers.size() - 1; i++) {
            int temp = listOfNumbers.get(i);
            for (int j = i + 1; j < listOfNumbers.size(); j++) {
                tempList = new ArrayList<>();
                tempList.add(temp);
                tempList.add(listOfNumbers.get(j));
                finalLIst.add(tempList);
            }

        }
        finalLIst.add(listOfNumbers);
        return finalLIst;
    }

    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(1, 2, 3);
        System.out.println(get_power_set(list));
        //Output : [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    }
}
