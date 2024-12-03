package HW2;

import java.util.Scanner;

public class Task7 {
    public static long factorial(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        System.out.println(factorial(ns.nextInt()));
    }
}
