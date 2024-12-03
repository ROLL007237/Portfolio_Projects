package HW4;

import java.util.Scanner;

import static java.lang.Math.pow;

public class Task4 {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        int n = ns.nextInt();
        int m = ns.nextInt();
        int res = 0;
        for (int i = 1; i <= m; i++) {
            double k = n%pow(10,i);
            System.out.println(k);
            res += (int) k;
        }
        System.out.println(res);
    }
}
