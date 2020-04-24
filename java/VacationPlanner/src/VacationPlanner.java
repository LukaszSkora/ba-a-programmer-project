import java.util.Scanner;

public class VacationPlanner {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        intro();
        budget();
        time();
        distance();
    }

    public static void intro() {
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to Vacation Planner!");
        System.out.print("What is your name? ");
        String name = input.nextLine();
        System.out.print("Nice to meet you " + name + ", where are you travelling to? ");
        String destination = input.nextLine();
        System.out.println("Great! " + destination + " sounds like a great trip");
        System.out.println("******************");
        System.out.println();
    }

    public static void budget() {
        Scanner input = new Scanner(System.in);
        System.out.print("How many days are you going to spent travelling? ");
        int days = input.nextInt();
        System.out.print("How much money, in USD, are you planning to spent on your trip? ");
        int money = input.nextInt();
        System.out.print("What is a tree letter currency symbol for your travel destination? ");
        String currencySymbol = input.next();
        System.out.print("How many " + currencySymbol + " are there in 1 USD? ");
        double exchangeRate = input.nextDouble();
        System.out.println();
        System.out.println("If you are travelling for " + days + " days that is the same as " + (days * 24) + " hours or " + (days * 24 * 60) + " minutes");
        System.out.println("If you are going to spend $" + money + " USD that means per day you can spend up to $" + (money / days) + " USD");
        //rounding to 2 decimal places
        double x = money * exchangeRate * 100;
        int y = (int) x;
        x = ((double) y) / 100;
        System.out.println("Your total budget in " + currencySymbol + " is " + x);
        System.out.println("******************");
        System.out.println();
    }

    public static void time() {
        Scanner input = new Scanner(System.in);
        System.out.print("What is the time difference, in hours, between your home and your destination? ");
        int timeDifference = input.nextInt();
        System.out.println("That means that when it is midnight at home it will be " + ((24 + timeDifference) % 24) + ":00 in your travel destination\nand when it is noon at home it will be " + (12 + timeDifference) + ":00");
        System.out.println("******************");
        System.out.println();
    }

    public static void distance() {
        Scanner input = new Scanner(System.in);
        System.out.print("What is the square area of your destination country in km2? ");
        //rounding to 2 decimal places
        double squareArea = input.nextDouble();
        double x = squareArea * 0.62137 * 100;
        int y = (int) x;
        x = ((double) y) / 100;
        System.out.println("In miles2 it is " + x);
    }
}
