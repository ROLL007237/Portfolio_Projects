package HW4;

import java.util.Scanner;

public class Task1b {
    public static void main(String[] args) {

        Scanner ns = new Scanner(System.in);
        int n = ns.nextInt();
        double res = 1.0;
        for (int i = 2; i <= n; i++) {
            res = res * (1.0 + 1.0/(n*n));
        }
        System.out.format("Result is %f", res);
    }
}