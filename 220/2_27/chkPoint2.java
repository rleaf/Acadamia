public class chkPoint2 {

   public static void main(String[] args) {

      // Checkpoint 1
      // chkOne();

      // Checkpoint 2
      chkTwo();

   }

   private static void chkOne() {

      int amount1 = 20, amount2 = 20;

   // if (amount1 > 10 && amount2 < 100) {
   //    System.out.println("this also works");
   // }

      if (amount1 > 10) {
         
         if (amount2 < 100) {
            
            System.out.println("toads");

         }
      }
   }

   private static void chkTwo() {

      int x = 5, y = 19, z = 9;

      if (x > 0) {
         if (y < 20) {
            z = 1;
         }
         else {
            z = 0;
         }
      }

      System.out.println(z);

   }

}