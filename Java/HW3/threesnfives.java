package HW3;

import java.util.Scanner;

public class threesnfives {
    public static void main(String[] args) {

        Scanner ns = new Scanner(System.in);

        int n = ns.nextInt();

        int fives = 1;
        int threes = 1;

        while (fives*5+threes*3 != n) {
            if (fives > 0 && threes < 3) {
                fives -= 1;
                threes += 2;
            } else {
                threes-= 3;
                fives += 2;
            }
        }
        System.out.format("There are %d fives and %d threes",fives,threes);
    }
}

