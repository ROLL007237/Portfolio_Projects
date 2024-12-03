package HW1;

import java.util.Scanner;

public class Task6 {

    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        float radius = ns.nextFloat();
        float x = ns.nextFloat();
        float y = ns.nextFloat();
        if (circle(x, y, radius) == 1) {
            System.out.println("Inside of circle");
        } else {
            System.out.println("Outside of circle");
        }
    }

    public static int circle(float x, float y, float radius) {
        if (Math.pow(x, 2) + Math.pow(y, 2) <= Math.pow(radius, 2)) {
            return 1;
        } else {
            return 0;
        }
    }
}
