/**
 * EmployeeDemo
 */
public class EmployeeDemo {

   public static void main(String[] args) {
      
      //  Instantiating objects
      Employee testOne = new Employee();
      Employee testTwo = new Employee();
      Employee testThree = new Employee();

      // Setting Object Attributes
      testOne.set("MD Ali", 12345, "Computer Science");
      testTwo.set("Sean Kane", 54321, "Information Technologoy");
      testThree.set("Nasir Jones", 13579, "Business");

      // Getting Object Attributes
      System.out.printf("%s %s %d \n", testOne.getName(), testOne.getDepartment(), testOne.getId());
      System.out.printf("%s %s %d \n", testTwo.getName(), testTwo.getDepartment(), testTwo.getId());
      System.out.printf("%s %s %d \n", testThree.getName(), testThree.getDepartment(), testThree.getId());


   }

}