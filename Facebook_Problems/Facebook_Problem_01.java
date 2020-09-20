/*
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
 */

import java.util.Random;

public class Facebook_Problem {
    public static int counter = 1;

    public static int getRandomElementFromStream(int[] array) {
        int num = 0;
        Random random = new Random();
        for (int e : array) {
            num = array[random.nextInt(counter)];
            counter++;
        }
        return num;
    }

    public static void main(String[] args) {
        int[] arr = {5, 0, 52, 18, 98, 32, 75, 94, 61, 3, 22};
        System.out.println(getRandomElementFromStream(arr));


    }
}
