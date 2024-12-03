package HW5;

import java.util.Arrays;
import java.util.Scanner;

public class BinarySearch {
    public static void main(String[] args) {

        Scanner ns = new Scanner(System.in);
        int len = ns.nextInt();
        int[] arr = new int[len];
        for (int i = 0; i < len; i++) {
            arr[i] = ns.nextInt();
        }
        int n = ns.nextInt();
        Arrays.sort(arr);
        System.out.println(binary_search(arr,n));
    }
    public static int binary_search(int[] arr, int n){
        int index = arr.length/2;
        if (arr[index] == n){
            return index;
        }
        if (arr[index] > n){
            arr = Arrays.copyOfRange(arr,0, index-1);
            return binary_search(arr, n);
        }else{
            arr = Arrays.copyOfRange(arr,index+1, arr.length);
            return binary_search(arr, n);
        }
    }
}
