package HW4;

import java.util.Scanner;

import static java.lang.Math.pow;

public class Task1 {
    public static void main(String[] args) {

        Scanner ns = new Scanner(System.in);
        int n = ns.nextInt();
        System.out.format("Result is %.1f",pow(2,n));
    }
}
