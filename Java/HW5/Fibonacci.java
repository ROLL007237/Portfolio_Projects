package HW5;

import java.util.Scanner;

import static java.lang.Math.pow;

public class Fibonacci {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        int len = ns.nextInt();
        int[] arr = new int[len];
        for (int i = 0; i < len; i++) {
            arr[i] = ns.nextInt();
        }
        boolean flag = false;
        for (int i = 0; i < len; i++) {

            int isqrd = 5 * arr[i] * arr[i];
            double iter1 = pow(isqrd - 4, 0.5);
            double iter2 = pow(isqrd + 4, 0.5);

            if (arr[0]*2 <= arr[1]){
                break;
            }

            if (iter1 == (int) iter1 || iter2 == (int) iter2){
                flag = (i <= 1 || arr[i] == arr[i - 1] + arr[i - 2]) ;
            }else{

                flag = false;
                break;
            }
        }
        if (flag){
            System.out.println("The array is a part of the Fibonacci sequence");
        }else{
            System.out.println("The array is not a part of the Fibonacci sequence");
        }
    }
}
