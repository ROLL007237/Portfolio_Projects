package HW3;

import java.util.Scanner;

public class Task5 {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);

        int n = ns.nextInt();
        int rem = 0;
        int quo = n;
        while (n > 0){
            int i = 1;
            n = n/10;
            if (n%10 == 0){
                rem *=10;
            }
            rem += n%10*i;
            i = i * 10;
            System.out.format("%d %d %d\n",n,rem,i);
        }
        if (quo == rem){
            System.out.format("Palindrome %d %d %d",n,rem,quo);
        }else{
            System.out.format("Not a palindrome %d %d %d",n,rem,quo);
        }
    }
}
