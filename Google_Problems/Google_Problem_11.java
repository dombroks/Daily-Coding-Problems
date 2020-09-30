/*
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
 */


public class Google_Problem_11 {
    public static int getEditDistance(String firstWord, String secondWord) {
        int editDistance = firstWord.length() - secondWord.length();
        if (editDistance < 0) {
            editDistance *= -1;
        }

        for (int i = 0; i < firstWord.length(); i++) {
            if (firstWord.charAt(i) != secondWord.charAt(i)) {
                editDistance++;
            }
        }


        return editDistance;
    }

    public static void main(String[] args) {
        String first = "kitten";
        String second = "sitting";
        System.out.println(getEditDistance(first, second));

    }
}
