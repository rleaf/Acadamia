public class sandbox {

    public static void main(String[] args) {
        
        short totalPay, basePay = 500, bonus = 1000;
        
        totalPay = (short)(basePay + bonus);
        
        System.out.println(totalPay);
        
        //        Challenge #2
        System.out.println("Challenge #2 ########################################");
        
        float alexa;
        double siri = 3.5;
        
        alexa = (float)(siri);
        
        System.out.println(alexa + "toads");
        
        //      Programming Challenge #2 - 
        System.out.println("Programming Challenge #2 ########################################");

        int fullPrice = 59;
        double sale = 0.2;

        System.out.println("The retail business sells product x at $" + fullPrice);
        System.out.println("The retail business sells product x at $" + (fullPrice - (fullPrice * 0.2)) + " after the 20% sale");
        System.out.println(fullPrice - (fullPrice * sale));

//      Programming Challenge #2 - Sales Prediction
        System.out.println("Programming Challenge #2 - Sales Prediction ########################################");

        double percentOfTotalSales = 0.62;
        double companyTotalSales = 4600000;

        System.out.println("The total predicted sales of the east coast company is: " + (companyTotalSales * percentOfTotalSales));

//      Programming Challenge #2 - Land Calculation
        System.out.println("Programming Challenge #2 - Land Calculation ########################################");
        int acre = 43560;
        int totalLand = 389767;

        System.out.println(totalLand / acre);

        



    }
}
