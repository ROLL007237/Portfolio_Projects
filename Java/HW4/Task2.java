package HW4;

import java.util.Scanner;

public class Task2 {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        float n = ns.nextFloat();
        float res = 1;
        int add = 2;
        while (res <= n){
            res += (float) 1.0/add;
            add += 1;
        }
        System.out.printf("Result = %.16f, add = %d", res, add);
    }
}
