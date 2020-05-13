import java.util.Scanner;
import java.util.Random;

public class rps {
   
   public static String userInput;
   public static String computerInput;
   public static int computerNumber;
   
   public static void main(String[] args) {
      // Ryan Lin, CSC 120 Final, Rock Paper Scissors Game
      
      Scanner input = new Scanner(System.in);
      Random random = new Random();

      System.out.println("This is a game of rock paper scissors,");
      
      System.out.println("Enter 'rock', 'paper', 'scissors'");
      String userInput = input.nextLine();

      computerNumber = random.nextInt(3) + 1;

      switch (computerNumber) {
         case 1:
            computerInput = "rock";
            break;
         case 2:
            computerInput = "paper";
            break;
         default:
            computerInput = "scissors";
            break;
      }


      System.out.println("The user picked "+ userInput);
      System.out.println("The computer picked " + computerInput);

      if ((userInput.equals("scissors") && computerInput.equals("paper")) || (userInput.equals("rock") && computerInput.equals("scissors")) || (userInput.equals("paper") && computerInput.equals("rock")) ) {
         System.out.println("User wins!");
      } else if ((userInput.equals("rock") && computerInput.equals("paper")) || (userInput.equals("paper") && computerInput.equals("scissors")) || (userInput.equals("scissors") && computerInput.equals("rock")) ) {
         System.out.println("Computer wins!");
      } else {
         System.out.println("The game is a tie!");
      }
      
   } 
}