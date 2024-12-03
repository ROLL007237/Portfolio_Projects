package HW1;

import java.util.Scanner;

public class Task7 {

    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        int num = ns.nextInt();

        if (num < 0) {
            System.out.println("Please enter a positive integer.");
        } else {
            String binaryString = Integer.toBinaryString(num);
            System.out.println("Binary: " + binaryString);

            int longestSeq = findLongestOnesSequence(binaryString);
            System.out.println("The longest sequence of '1's: " + longestSeq);
        }

    }

    public static int findLongestOnesSequence(String binaryString) {
        String[] sequences = binaryString.split("0");
        int maxLength = 0;

        for (String seq : sequences) {
            if (seq.length() > maxLength) {
                maxLength = seq.length();
            }
        }

        return maxLength;

    }
}