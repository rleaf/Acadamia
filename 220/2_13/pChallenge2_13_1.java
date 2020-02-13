import java.util.Scanner;

/**
 * pChallenge2_13_1
 * 
 *  Ryan Lin, CSC 120, 2_13_20
 * 
 */
public class pChallenge2_13_1 {

   public static void main(final String[] args) {

      double nMales;
      double nFemales;
      double totalClassBody;
      int pMales;
      int pFemales;

      final Scanner keyboard = new Scanner(System.in);

      System.out.println("Enter the number of males in the class:");
      nMales = keyboard.nextDouble();

      System.out.println("Enter the number of females in the class:");
      nFemales = keyboard.nextDouble();

      totalClassBody = nMales + nFemales;
      pMales = (int)(nMales / totalClassBody * 100);
      pFemales = (int)(nFemales / totalClassBody * 100);
      
      // System.out.printf("Hello %d", pMales);
      System.out.printf("%d percent of the class is female, %d percent of the class is male %n", pFemales, pMales);

   }
}