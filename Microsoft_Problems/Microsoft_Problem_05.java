/*
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
 */

import java.util.ArrayList;
import java.util.List;

public class Microsoft_Problem_05 {
    public static List<String> getWordsFromMatrix(char[][] matrix) {
        List<String> words = new ArrayList<>();

        for (int i = 0; i < matrix.length; i++) {
            String horizontal = "";
            String vertical = "";
            for (int j = 0; j < matrix.length; j++) {
                vertical = vertical + matrix[i][j];
                horizontal = horizontal + matrix[j][i];
            }
            words.add(vertical);
            words.add(horizontal);
        }
        return words;
    }


    public static boolean isExisted(String word, List<String> words) {
        return words.contains(word);
    }

    public static void main(String[] args) {
        char[][] matrix = {
                {'F', 'A', 'C', 'I'},
                {'O', 'B', 'Q', 'P'},
                {'A', 'N', 'O', 'B'},
                {'M', 'A', 'S', 'S'}
        };
        assert isExisted("FOAM", getWordsFromMatrix(matrix));
        assert isExisted("MASS", getWordsFromMatrix(matrix));
        assert !isExisted("DELL", getWordsFromMatrix(matrix));

    }
}
