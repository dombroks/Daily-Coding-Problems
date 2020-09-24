/*
This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
*/

public class Facebook_Problem_03 {

    public static boolean isMatch(String word, String regex) {
        boolean match = false;
        if (regex.isEmpty() || word.isEmpty()) return false;

        if (regex.contains(".")) {
            if (word.length() > regex.indexOf(".") + 1) {
                match = false;
            } else {
                match = true;
            }
        }
        if (regex.contains("*")) {
            String subWord = regex.substring(regex.indexOf("*"))
                    .replace("*", "");

            if ((word.substring(0, word.indexOf(subWord)).length() + subWord.length()) < word.length()) {
                match = false;
            } else
                match = true;
        }

        return match;
    }

    public static void main(String[] args) {
        System.out.println("Test with ray and ra.");
        String word = "ray";
        String regex = "ra.";
        System.out.println(isMatch(word, regex));
        System.out.println("---------");
        System.out.println("Test with chats and .*at");
        word = "chats";
        regex = ".*at";
        System.out.println(isMatch(word, regex));


    }
}
