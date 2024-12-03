package HW5;

import java.util.Arrays;
import java.util.Scanner;

public class Task1 {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        int len = ns.nextInt();
        int[] arr = new int[len];
        for (int i = 0; i < len; i++) {
            arr[i] = ns.nextInt();
        }
        arr = Arrays.copyOfRange(arr,0,2);
        System.out.println(Arrays.toString(arr));
    }
}
