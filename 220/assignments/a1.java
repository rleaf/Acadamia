/**
 * a1
 * 
 * Ryan Lin, CSC 120, Assignment 1
 * 
 */

import java.util.Scanner;

public class a1 {
   
   public static void main(final String[] args) {

      /**
       * Test Average section of Assignment 1 - Section 1
       */
      
      int testOne, testTwo, testThree;
      
      final Scanner keyboard = new Scanner(System.in);

      System.out.println("Test 1 score:");
      testOne = keyboard.nextInt();

      System.out.println("Test 2 score:");
      testTwo = keyboard.nextInt();

      System.out.println("Test 1 score:");
      testThree = keyboard.nextInt();

      System.out.printf("Test one score: %d%nTest two score: %d%nTest three score: %d%n", testOne, testTwo, testThree);
      System.out.println("The average test score is: " + ((testOne + testTwo + testThree) / 3) );



      stringManipulator();
      restaurantBill();
      wordGame();
   }

   public static void stringManipulator() {

      /**
       * String Manipulator section of Assignment 1 - Section 2
       */

      String favCity;

      final Scanner keyboard = new Scanner(System.in);     

      System.out.println("Enter the name of your favorite city:");
      favCity = keyboard.nextLine();

      System.out.println("Length: " + favCity.length());
      System.out.println("Uppercase: " + favCity.toUpperCase());
      System.out.println("Lowercase: " + favCity.toLowerCase());
      System.out.println("First letter: " + favCity.charAt(0));

   }

   public static void restaurantBill() {

      /**
       * Restaurant Bill section of Assignment 1 - Section 3
       */
      
      double bill, totalBill, tax, tip;
      final double taxRate = 0.565, tipRate = 0.2;

      final Scanner keyboard = new Scanner(System.in);

      System.out.println("Enter the bill: ");
      bill = keyboard.nextDouble();

      tax = bill * taxRate;
      tip = (bill + tax) * tipRate;
      totalBill = bill + tax + tip;

      System.out.println("Your tax is: " + tax);
      System.out.println("Your tip is: " + tip);
      System.out.println("Your total bill is: " + totalBill);

   }

   public static void wordGame() {

      /**
       * Word Game section of Assignment 1 - Section 4
       */
      
      int age;
      String name, nameOfCity, nameOfCollege, profession, animal, petName;

      final Scanner keyboard = new Scanner(System.in);

      System.out.println("Enter a name: ");
      name = keyboard.nextLine();
      
      System.out.println("Enter an age: ");
      age = keyboard.nextInt();

      // Scanner.nextInt() does not consume '\n' character
      keyboard.nextLine(); 
      
      System.out.println("Enter a name of a city: ");
      nameOfCity = keyboard.nextLine();
      
      System.out.println("Enter a name of a college: ");
      nameOfCollege = keyboard.nextLine();
      
      System.out.println("Enter a profession: ");
      profession = keyboard.nextLine();
      
      System.out.println("Enter an animal: ");
      animal = keyboard.nextLine();
      
      System.out.println("Enter a pet name: ");
      petName = keyboard.nextLine();

      System.out.printf("There once was a person named %s who lived in %s. At the age of %d, %s went to college at %s. %s graduated and went back to work as a %s. Then, %s adopted an %s named %s. They both lived happily ever after!", name, nameOfCity, age, name, nameOfCollege, name, profession, name, animal, petName);
   }
}