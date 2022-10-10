package graphs;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        double x0 = 1;
        double y0 = 2;
        double r0 = 5;

        List<List<Double>> series = create_series(x0,y0, r0);
        List<List<Double>> eps = create_eps(series);

        List<Double> sums = new ArrayList<Double>();
        List<Double> eps_sums = new ArrayList<Double>();

        for(int i = 0; i < series.size(); i++){
            sums.add((series.get(0).get(i) + series.get(1).get(i) + series.get(2).get(i) + series.get(3).get(i) + series.get(4).get(i)) / series.size());
            eps_sums.add(Math.abs((sums.get(i) - Math.PI) / Math.PI));
        }

        for(int i = 0; i < 5; i++){
            for(int ser = 0; ser < 5; ser++)
                System.out.println("f\"series[" + i + "]" +
                        "[" + ser + "] is " + series.get(i).get(ser));
        }
        System.out.println();
        for(int i = 0; i < 5; i++)
            System.out.println("f\"eps[" + i + "]" + " is " + eps.get(i));
        System.out.println();
        for(int i = 0; i < 5; i++)
            System.out.println("f\"sums[" + i + "]" + " is " + sums.get(i));
        System.out.println();
        for(int i = 0; i < 5; i++)
            System.out.println("f\"eps_sums[" + i + "]" + " is " + eps_sums.get(i));

        }


    public static double calc_pi(double x0, double y0, double r0, double exp_nmb){

        int m = 0;
        double minX = x0 - r0;
        double maxX = x0 + r0;
        double minY = y0 - r0;
        double maxY = y0 + r0;

        double result_pi = 0;

        for (int exp = 0; exp < exp_nmb; exp++){
            double p = Math.random();
            double xp = (maxX - minX) * p + minX;
            p = Math.random();
            double yp = (maxY - minY) * p + minY;

            if(Math.pow((xp - x0), 2) + Math.pow((yp - y0), 2) < Math.pow(r0, 2))
                m+=1;
        }
        result_pi = (4 * m )/exp_nmb;
        return result_pi;
    }
    public static List<List<Double>> create_series(double x0, double y0, double r0){
        List<List<Double>> series = new ArrayList<List<Double>>();
        for(int num = 0; num < 5; num++){

            ArrayList<Double> seria = new ArrayList<Double>();

            for(int power = 4; power < 9; power++){
                double exp_nmb = Math.pow(10,power);
                seria.add(calc_pi(x0, y0, r0, exp_nmb));
            }
            series.add(seria);
        }
        return series;

    }
    public static double calculate_eps(double seria){
        return Math.abs((seria - Math.PI) / Math.PI);
    }
    public static List<List<Double>> create_eps(List<List<Double>> series){
        List<List<Double>> eps = new ArrayList<List<Double>>();
        for (List<Double> s : series) {
            ArrayList<Double> curent_eps = new ArrayList<Double>();
            for( double calculated_pi : s)
                curent_eps.add(calculate_eps(calculated_pi));
            eps.add(curent_eps);
        }
        return eps;
    }
}

