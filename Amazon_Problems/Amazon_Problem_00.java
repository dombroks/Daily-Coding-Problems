/*
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
*/




import java.util.ArrayList;

public class Amazon_Problem_00 {
    public static int getUniqueCharactersNumber(String word) {
        ArrayList<Character> chars = new ArrayList<Character>();
        for (int i = 0; i < word.length(); i++) {
            if (!chars.contains(word.charAt(i))) {
                chars.add(word.charAt(i));
            }
        }
        return chars.size();

    }

    public static String getLongestSubstring(String s, int k) {
        int max = 0, begin = 0;
        String Substring = "";
        while (begin < s.length()) {
            for (int i = k; i < s.length(); i++) {
                String temp;
                int n = 0;
                temp = s.substring(begin, i);
                n = getUniqueCharactersNumber(temp);
                if (n > k) break;
                else {
                    if (temp.length() > max) {
                        max = temp.length();
                        Substring = temp;
                    }
                }

            }
            begin++;
            k++;
        }
        return Substring;


    }

    public static void main(String[] args) {
        System.out.println(getLongestSubstring("abcba", 2));
        System.out.println(getLongestSubstring("abbbdkn", 3));
    }
}
