package HW2;

import java.util.Scanner;

public class Task3 {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        int num = ns.nextInt();
        int res = num >= 5? (num - 2):(num*num);
        System.out.println(res);
    }
}
