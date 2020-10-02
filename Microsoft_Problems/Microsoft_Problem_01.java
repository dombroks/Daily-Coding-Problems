/*
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2

 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Microsoft_Problem_01 {
    public static void getMedians(int[] array) {
        List<Integer> tempList = new ArrayList<>();

        for (int i = 0; i < array.length; i++) {

            tempList.add(array[i]);
            Collections.sort(tempList);

            if (tempList.size() == 1) System.out.println(tempList.get(0));
            else {
                if (tempList.size() % 2 == 0) {
                    int size = tempList.size();
                    int middle = size / 2;
                    System.out.println((double) ((tempList.get(middle - 1)) + (tempList.get(middle))) / 2);

                } else System.out.println(tempList.get(tempList.size() / 2));
            }
        }


    }


    public static void main(String[] args) {
        int[] arr = {2, 1, 5, 7, 2, 0, 5};
        getMedians(arr);
    }
}
