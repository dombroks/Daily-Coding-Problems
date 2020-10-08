/*
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
 */
public class Amazon_Problem_02 {
    public static String encode(String s) {
        int n = s.length();

        String encodedMessage = "";
        for (int i = 0; i < n; i++) {
            // Count occurrences of current character
            int count = 1;
            while (i < n - 1 && s.charAt(i) == s.charAt(i + 1)) {
                count++;
                i++;
            }
            encodedMessage = encodedMessage + s.charAt(i) + count;
        }

        return encodedMessage;
    }


    public static String decode(String s) {
        String decodedMessage = "";
        for (int i = 0; i < s.length(); i = i + 2) {
            int temp = Integer.parseInt(String.valueOf(s.charAt(i)));

            for (int j = 0; j < temp; j++) {
                decodedMessage = decodedMessage + (char) s.charAt(i + 1);
            }
        }


        return decodedMessage;
    }

    public static void main(String[] args) {

        System.out.println("Decoded message is : " + decode("4A3B2C1D2A"));
        System.out.println("Encoded message is : " + encode("AAAABBBCCDAA"));
    }
}
