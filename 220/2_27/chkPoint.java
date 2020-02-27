public class chkPoint {

   public static void main(String[] args) {

      // Checkpoint 1
      chkOne();

      // Checkpoint 2
      chkTwo();

      // Checkpoint 3
      chkThree();

      // Checkpoint 4
      chkFour();

   }

   private static void chkOne() {

      boolean max = true;
      int fees;

      if (max) {
         fees = 50;
      }
      
   }

   private static void chkTwo() {

      int x = 101;
      int y = 3;
      int z = 3;

      if (x > 100) {
         y = 20;
         z = 40;
      }

      System.out.println(y + z);

   }

   private static void chkThree() {

      int a, b, c;

      if (a < 10) {
         b = 0;
         c = 1;
      }

      System.out.println();

   }

   private static void chkFour() {

      String myCharacter;

      if (myCharacter == "D") {
         System.out.println("Success");
      }

   }

}