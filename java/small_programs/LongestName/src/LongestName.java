/* The program takes n strings as an input and evaluates which is the longest.
   n is  provided as an input from the user.
   In case there is a tie, the program returns a message that there was one.
 */

import java.util.Scanner;

public class LongestName {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("How many names you want to check? ");
        int n = console.nextInt();
        longestName(console, n);
    }

    public static void longestName(Scanner console, int n) {
        String name = "";
        String longest = "";
        Boolean isTie = false;
        for (int i = 1; i <= n; i++) {
            System.out.print("name #" + i + "? ");
            name = console.next();
            if (name.length() > longest.length()) {
                longest = name;
                isTie = false;
            } else if (name.length() == longest.length()) {
                isTie = true;
            }
        }
        longest = longest.toLowerCase();
        longest = longest.substring(0, 1).toUpperCase() + longest.substring(1);
        // Alternative solution
        // longest = Character.toUpperCase(longest.charAt(0)) + longest.substring(1);
        System.out.println(longest+"'s name is longest");
        if (isTie) {
            System.out.println("(There was a tie!)");
        }
    }
}