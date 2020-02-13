public class retailPriceSale {

    public static void main(String[] args) {

        int fullPrice = 59;
        double sale = 0.2;

        System.out.println("The retail business sells product x at $" + fullPrice);
        System.out.println("The retail business sells product x at $" + (fullPrice - (fullPrice * 0.2))  + " after the 20% sale");
        System.out.println(fullPrice - (fullPrice * sale));
    }


}
