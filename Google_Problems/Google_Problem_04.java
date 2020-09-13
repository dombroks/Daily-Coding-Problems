/*
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
 */
public class Google_Problem_04 {


    public static String estimatePi(Long interval) {
        int numberOfCirclePoints = 0, numberOfSquarePoints = 0;
        double x, y, distance, Pi;
        for (int i = 0; i < Math.pow(interval, 2); i++) {
            x = getRandomNumber();
            y = getRandomNumber();

            distance = Math.pow(x, 2) + Math.pow(y, 2);
            if (distance <= 1) {
                numberOfCirclePoints++;
            }
            numberOfSquarePoints++;

        }
        Pi = (double) (4 * numberOfCirclePoints) / numberOfSquarePoints;


        return String.format("%.3f", Pi);
    }

    private static double getRandomNumber() {
        return ((Math.random() * (1.0 - (-1.0))) + (-1.0));
    }

    public static void main(String[] args) {
        Long interval = 10L;
        System.out.println(estimatePi(interval));

    }
}
