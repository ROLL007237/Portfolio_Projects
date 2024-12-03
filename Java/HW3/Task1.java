package HW3;

import java.util.Scanner;

import static java.lang.Math.pow;

public class Task1 {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        System.out.println("Write in distance between objects,velocities of objects and accelerations of objects in that order\n1. Distance\n2.Velocity 1/2\n3.Acceleration 1/2\n");
        float dist = ns.nextFloat();
        float startv1 = ns.nextFloat();
        float startv2 = ns.nextFloat();
        float a1 = ns.nextFloat();
        float a2 = ns.nextFloat();
        float over_v = startv1+startv2;
        float over_a = a1+a2;
        System.out.println(formula(dist,over_a,over_v));

    }
    public static double formula(float dist, float over_a, float over_init_v){
        if (over_a == 0){
            return dist/over_init_v;
        }else{
            return -over_init_v + pow(over_init_v*over_init_v + 2*over_a*dist, 0.5);
        }
    }
}
