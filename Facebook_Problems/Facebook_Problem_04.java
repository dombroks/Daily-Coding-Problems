/*
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
 */

import java.util.*;

public class Facebook_Problem_04 {
    public static boolean areBalanced(String s) {
        int len = s.length();
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> map = new HashMap();
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');

        for (char c : s.toCharArray()) {
            if (len > 0 && map.containsKey(c) && stack.lastElement() == map.get(c)) {
                stack.pop();
            } else
                stack.push(c);
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        String s = "((()))[]";
        System.out.println(areBalanced(s));
    }
}
