package HW2;

import java.util.Scanner;

public class Task6 {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        int num = ns.nextInt();
        String res = switch (num/10){
            case 5 -> "Failed";
            case 6 -> "Three";
            case 7 -> "Four";
            case 8 -> "Five";
            default -> throw new IllegalArgumentException("Invalid score");
            };
        System.out.println(res);
        }
}

//Its just inefficient to do this with switch case