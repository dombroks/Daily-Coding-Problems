/*
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
 */


import java.util.Random;

public class Twitter_Problem_01 {

    static class CustomizedBuffer {
        int[] ids;
        int numberOfRecords;
        int endPointer;

        public CustomizedBuffer(int numberOfRecords) {
            this.numberOfRecords = numberOfRecords;
            this.ids = new int[numberOfRecords];
            this.endPointer = 0;
        }

        public void record(int orderId) {
            ids[endPointer] = orderId;
            endPointer = ++endPointer % numberOfRecords;
        }

        public int get_last(int i) {
            if (i <= endPointer) {
                return ids[endPointer - i];
            } else
                return ids[(endPointer - i) + numberOfRecords];

        }

    }

    public static void main(String[] args) {
        Random random = new Random();
        CustomizedBuffer buffer = new CustomizedBuffer(12);
        for (int i = 0; i < buffer.numberOfRecords; i++) {
            //fill the buffer with random numbers between 0 and 100
            buffer.record(random.nextInt(100));
            //print buffer elements
            System.out.println(buffer.ids[i]);
        }
        int number = 2;
        System.out.println("the " + number + "th last element is: " + buffer.get_last(number));
    }
}
