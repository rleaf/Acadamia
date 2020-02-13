import java.util.Scanner;

/**
 * test2
 */
public class test2 {

   public static void main(String[] args) {
      // System.out.println("toaders");

      Scanner keyboard = new Scanner(System.in);
      System.out.println("Enter a name: ");

      String uName = keyboard.nextLine();
      System.out.println("Hello" + uName);
   }
}