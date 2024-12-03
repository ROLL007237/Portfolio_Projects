package HW2;

import java.util.Scanner;

public class Task1 {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        int num = ns.nextInt();
        String res = num%2==0 ? "Even":"Odd";
        System.out.println(res);
    }
}
