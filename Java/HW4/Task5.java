package HW4;

import java.util.Scanner;


public class Task5 {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        int n = ns.nextInt();
        int n1= n*n;
        while (n1>0){
            if (n1%10 == 3){
                System.out.println("THERE IS");
                break;
            }
            n1 /= 10;
        }
    }
}
