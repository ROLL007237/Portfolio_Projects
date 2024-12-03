package HW1;

import java.util.Scanner;

public class Task5 {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        int num = ns.nextInt();
        int res = 0;
        while (num > 0) {
            res += num % 10;
            num /= 10;
        }
        System.out.println(res);
    }
}
