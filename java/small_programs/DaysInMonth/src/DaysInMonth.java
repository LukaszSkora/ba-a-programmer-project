/* The program evaluates how many days are in a given month.
   The month is provided by the user by inputting a month's number.
 */

import java.util.Scanner;

public class DaysInMonth {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter month number: ");
        int monthNo = input.nextInt();
        System.out.println(monthNo);
        daysInMonth(monthNo);
    }

    public static int daysInMonth(int monthNo) {
        if (monthNo == 1 || monthNo == 3 || monthNo == 5 || monthNo == 7 || monthNo == 8 || monthNo == 10 || monthNo == 12) {
            return 31;
        } else if (monthNo == 2) {
            return 28;
        } else {
            return 30;
        }
    }
}
