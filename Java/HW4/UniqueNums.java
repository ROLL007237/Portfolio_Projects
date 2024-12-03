package HW4;

import java.util.Arrays;
import java.util.Scanner;

public class UniqueNums {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        int len = ns.nextInt();
        int[] arr = new int[len];
        for (int i = 0; i < len; i++) {
            arr[i] = ns.nextInt();
        }

        int[] arrSorted = sort(arr);
        int counter = 1;

        System.out.println(Arrays.toString(arrSorted));
        int prev = arrSorted[0];
        for (int i = 1; i < arrSorted.length; i++) {
            if (arrSorted[i] == prev){
                counter+=1;
            }else{
                System.out.println(counter + " " + arrSorted[i-1]);
                counter = 1;
            }
            prev = arrSorted[i];
        }
        System.out.println(counter + " " + arrSorted[arr.length-1]);

    }

    private static int[] sort(int[] arr){
        for (int i = 0; i < arr.length; i++) {
            for (int j = arr.length-1; j > 0; j--) {
                if (arr[j] < arr[j-1]){
                    int buf = arr[j];
                    arr[j] = arr[j-1];
                    arr[j-1] = buf;
                }
            }
        }
        return arr;
    }
}
