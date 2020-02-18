public class LengthWidthDemo {

    public static void main(String[] args) {

        Rectangle box = new Rectangle();
        System.out.println("Sending the value 10.0 to the setLength method.");

        box.setLength(10.0);
        System.out.println("Done. Length = " + box.getLength());


        System.out.println("Sending the value 20.0 to the setWidth method.");

        box.setWidth(20.0);
        System.out.println("Done. Width = " + box.getWidth());
    }

}
