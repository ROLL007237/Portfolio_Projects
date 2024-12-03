package HW3;

import java.util.Scanner;

public class Task2 {
    public static void main(String[] args) {

        Scanner ns = new Scanner(System.in);

        float[] arr;
        arr = new float[3];

        arr[0] = ns.nextFloat();
        arr[1] = ns.nextFloat();
        arr[2] = ns.nextFloat();

        float max = -9999;
        float min = 9999;

        for (int i = 0; i<3; i++){
            if (arr[i]>max){
                max = arr[i];
            }
            if (arr[i] < min){
                min = arr[i];
            }
        }
        System.out.println("max - "+max+"\nmin - "+min);
    }
}
