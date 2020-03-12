public class nestedFor {


   public static void main(String[] args) {
      
      int x = 0;

      for (int i = 1; i < 3; i++) {
         for (int j = 1; j < 3; j++) {
            x = i * j;
            System.out.println(x);

         }
      }

   }

}