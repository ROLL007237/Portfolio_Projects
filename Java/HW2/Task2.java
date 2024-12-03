package HW2;

import java.util.Scanner;

public class Task2 {
    public static void main(String[] args) {
        System.out.println("Write a number: ");
        Scanner ns = new Scanner(System.in);
        int num = ns.nextInt();
        String res;
        res = num<0? "Negative"
                : num>0? "Positive"
                :"Zero";
        System.out.println(res);
    }
}
