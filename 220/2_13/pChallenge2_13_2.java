import java.util.Scanner;

/**
 * pChallenge2_13_2
 * 
 * Ryan Lin, CSC 120, 2_13_20
 * 
 * 1.5 cups of sugar
 * 1 cup of butter
 * 2.75 cups of flour
 * 
 * 5.25 total cups of material == 48 cookies || 0.109 cups per cookie
 * 
 * 28.5% == amount of sugar / cup
 * 19.0% == amount of butter / cup
 * 52.3% == amount of flour / cup
 * 
 */
public class pChallenge2_13_2 {

   public static void main(final String[] args) {

      int inputCookieAmount;
      double sugarAmount, butterAmount, flourAmount, cupsRequired;
      final double sugarPercent = .285, butterPercent = .190, flourPercent = .523;
      final double cupsPerCookie = 0.109375;

      final Scanner keyboard = new Scanner(System.in);

      System.out.println("How many cookies do you want to make? ");
      inputCookieAmount = keyboard.nextInt();

      cupsRequired = cupsPerCookie * inputCookieAmount;
      sugarAmount = sugarPercent * cupsRequired;
      butterAmount = butterPercent * cupsRequired;
      flourAmount = flourPercent* cupsRequired;


      System.out.printf("You will need %.2f cups of sugar, %.2f cups of butter, and %.2f cups of flousr", sugarAmount, butterAmount, flourAmount);
      
   } 

}