package HW1;

import java.util.Scanner;

public class Task4 {
    public static void main(String[] args) {
        int prev = -999999999;
        while (true) {
            Scanner ns = new Scanner(System.in);
            int num = ns.nextInt();
            if (num >= prev) {
                System.out.println(num);
                prev = num;
            } else {
                break;
            }
        }
    }
}
