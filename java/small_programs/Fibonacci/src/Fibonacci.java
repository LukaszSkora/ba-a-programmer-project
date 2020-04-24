/* The program returns a list of n numbers in Fibonacci sequence.
   n is specified by the user.
 */

import java.util.Scanner;

public class Fibonacci {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an integer (which will be the n-th number in Fibonacci sequence): ");
        int input = scanner.nextInt();
        for (int i = 1; i <= input; i++) {
            System.out.println("For number " + i + " the sum of Fibonacci sequence is: " + fibonacci(i));
        }
    }

    public static int fibonacci(int num) {
        if (num == 1 || num == 2) {
            return 1;
        }
        return num = fibonacci(num - 1) + fibonacci(num - 2);
    }
}
