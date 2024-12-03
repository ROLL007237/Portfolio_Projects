package HW2;

import java.util.Scanner;

public class Task4 {
    public static void main(String[] args) {


        Scanner ns = new Scanner(System.in);
        int num = ns.nextInt();
        String res = num <5? "Little"
                : num > 10? "Large"
                : "Middle";
        System.out.println(res);
    }
}