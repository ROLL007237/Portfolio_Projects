package HW3;

import java.util.Scanner;
import java.util.Arrays;


public class Task3 {
    public static void main(String[] args) {

        Scanner ns = new Scanner(System.in);

        float[] arr;
        arr = new float[3];

        arr[0] = ns.nextFloat();
        arr[1] = ns.nextFloat();
        arr[2] = ns.nextFloat();

        Arrays.sort(arr);

        if (arr[0] < arr[1]+arr[2] && arr[1] < arr[2]+arr[0] && arr[2] < arr[1]+arr[0]) {
            if (arr[0]*arr[0] < arr[1]*arr[1] + arr[2]*arr[2]) {
                System.out.println("acute-angled");
            }
            System.out.println("exists");
        }else{
            System.out.println("does not exist");
        }
    }
}