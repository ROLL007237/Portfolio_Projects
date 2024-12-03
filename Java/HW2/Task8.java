package HW2;

import java.util.Arrays;

public class Task8 {
    public static float mean(int[] n){
        int len = n.length;
        int sum = Arrays.stream(n).sum();
        return (float) sum /len;
    }

    public static void main(String[] args) {
        int[] myArr = new int[] {0,5,4,10};
        System.out.println(mean(myArr));
    }
}
