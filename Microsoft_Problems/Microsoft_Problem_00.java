/*
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
 */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Microsoft_Problem_00 {


    public static List<String> getOriginalSentence(String[] dict, String sentence) {
        Map map = new HashMap();
        List<String> original = new ArrayList<>();
        for (String word : dict) {
            if (sentence.contains(word)) {
                map.put(sentence.indexOf(word), word);
            }
        }
        for (Object i : map.values()) {
            original.add(i.toString());
        }
        return original;

    }

    public static void main(String[] args) {
        String[] dict = new String[]{"bed", "bath", "bedbath", "and", "beyond"};
        String sentence = "bedbathandbeyond";

        String[] dict2 = new String[]{"quick", "brown", "the", "fox"};
        String sentence2 = "thequickbrownfox";


        System.out.println(getOriginalSentence(dict, sentence));
        System.out.println(getOriginalSentence(dict2, sentence2));

    }
}
