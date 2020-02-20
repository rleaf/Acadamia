public class Employee {

   private String _name;
   private String _department;
   private int _idNumber;


   // Setters

   // public void setName(String name) {
   //    _name = name;
   // }

   // public void setDepartment(String department) {
   //    _department = department;
   // }

   // public void setId(double idNumber) {
   //    _idNumber = idNumber;
   // }

   public void set(String name, int idNumber, String department) {
      _name = name;
      _department = department;
      _idNumber = idNumber;
   }
   
   //  Getters

   public String getName() {
      return _name;
   }

   public String getDepartment() {
      return _department;
   }

   public int getId() {
      return _idNumber;
   }

}