package HW5;

import java.util.Scanner;

public class IfI {
    public static void main(String[] args) {

        Scanner ns = new Scanner(System.in);
        String str = ns.nextLine();
        char[] chars = str.toCharArray();
        boolean flag = false;

        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == 'i'){
                flag = true;
                break;
            }
        }
        System.out.println(flag);
    }
}
