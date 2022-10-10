package graphs;

import java.util.ArrayList;
import java.util.List;


public class Main {

    public static void main(String[] args) {
        List<Double> series = creationOfSeries();
        List<List<Double>> listOfEps = creationOfEps(series);
        double sum = 0;
        double epsSum = 0;

        for (int i = 0; i < series.size(); i++){
            double sumOfSeries = 0;
            for (double s : series)
                sumOfSeries += s;
            sum = (sumOfSeries / series.size());
            epsSum = Math.abs(sum - 6) / 6;
        }

        for(int i = 0; i < 5; i++){
            System.out.println("f\"series[" + i + "] is " + series.get(i));
        }

        System.out.println();
        for(int i = 0; i < 5; i++)
            System.out.println("f\"eps[" + i + "]" + " is " + listOfEps.get(i));
        System.out.println();
        System.out.println("f\"sums is " + sum);
        System.out.println();
        System.out.println("f\"eps_sums is " + epsSum);

    }

    public static double function(double x){
        return Math.pow(x, 3) + 1;
    }

    public static List<Double> creationOfSeries(){
        List<Double> series = new ArrayList<Double>();
        for (double i = 3; i <= 8; i++){
            series.add(calculationOfIntegral(0, 2, Math.pow(10, i)));
        }
        return series;
    }

    public static double calculationOfIntegral(double a, double b, double exp_nmb){
        double minX = a;
        double maxX = b;
        double minY = 0;
        double maxY = function(b);
        double m = 0;

        for(int i = 0; i < exp_nmb; i++){
            double p = Math.random();
            double xp = (maxX - minX) * p + minX;
            p = Math.random();
            double yp = (maxY - minY) * p + minY;

            if (function(xp) > yp)
                m+=1;
        }

        return m * (b - a) * function(b) / exp_nmb;
    }

    public static double calculationOfEps(double seria){
        return Math.abs((seria - 6) / 6);
    }

    public static List<List<Double>> creationOfEps(List<Double> series){
        List<List<Double>> eps = new ArrayList<List<Double>>();
        for (double s:
                series) {
            ArrayList<Double> currentEps = new ArrayList<Double>();
            currentEps.add(calculationOfEps(s));
            eps.add(currentEps);

        }
        return eps;
    }


}

