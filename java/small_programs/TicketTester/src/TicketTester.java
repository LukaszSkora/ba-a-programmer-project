/* The program checks if persons are qualified to buy a ticket.
   The program evaluates whether the person is qualified and returns appropriate message.
   The program summarises the result giving:
      - total number of persons allowed
      - total number of persons not allowed
      - the percentage of persons allowed
 */

import javax.swing.*;

public class TicketTester {
    public static void main(String[] args) {
        int entry = 0;
        int noEntry = 0;

        for (int i = 1; i <= 5; i++) {
            String string = JOptionPane.showInputDialog("What's your age?");
            int age = Integer.parseInt(string);

            if (age > 18) {
                entry = entry + 1;
                System.out.println(age + ": Entry");
            } else {
                noEntry = noEntry + 1;
                System.out.println(age + ": No entry");
            }
        }
        System.out.println(noEntry + " are not allowed entry");
        System.out.println(entry + " are allowed entry");
        System.out.println((int) (((double) entry / 5.0) * 100.0) + "% made it into the program");
    }
}
