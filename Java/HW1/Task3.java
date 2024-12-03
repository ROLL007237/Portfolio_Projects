package HW1;

import java.util.Scanner;

public class Task3 {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        float x = ns.nextFloat();
        float y = ns.nextFloat();
        float n = ns.nextFloat();
        if ((Math.abs(x) <= n / 2) || (Math.abs(y) <= n / 2)) {
            System.out.println("Inside of square");
        } else {
            System.out.println("Outside of square");
        }
    }
}
