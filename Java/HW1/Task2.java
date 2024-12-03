package HW1;

import java.util.Objects;
import java.util.Scanner;
public class Task2 {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        String word = ns.nextLine();
        if (Objects.equals(word, "Hello")){
            System.out.println("World!");}
        else{
            System.out.println("I don`t know this command");}
    }
}
