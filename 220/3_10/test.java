public class test {

   public static void main(String[] args) {
      
      // int x = 0;

      // for (int count = 10; count <= 21; count++) {
      //    // System.out.println(count);
      //    System.out.println(x++);

      // }

      toadies();
   }

   public static void toadies() {

      int x = 10;

      switch (x) {
         case 10:
            x += 15;
            break;
         case 12:
            x -= 5;
         default:
            break;
      }

      System.out.println(x);

   }

}