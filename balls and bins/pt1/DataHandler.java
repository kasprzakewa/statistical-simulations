import java.io.FileNotFoundException;
import java.io.PrintWriter;

public class DataHandler
{
    public void run() 
    {
        PrintWriter printWriter;

        try 
        {
            printWriter = new PrintWriter("data.txt");

            for (int n = 1000; n < 100001; n += 1000) 
            {
                double average;
                int b = 0;
                int u = 0;
                int c = 0;
                int d = 0;
                int d_c = 0;

                for (int k = 0; k < 50; k++) 
                {
                    Simulation simulation = new Simulation();
                    int[] results;

                    results = simulation.simulate(n);

                    printWriter.println(n + " " + results[0] + " " + results[1] + " " + results[2] + " " + results[3] + " " + results[4]);

                    b += results[0];
                    u += results[1];
                    c += results[2];
                    d += results[3];
                    d_c += results[4];
                }

                printWriter.print(n + " ");
                average = b / 50.0;
                printWriter.print(average + " ");
                average = u / 50.0;
                printWriter.print(average + " ");
                average = c / 50.0;
                printWriter.print(average + " ");
                average = d / 50.0;
                printWriter.print(average + " ");
                average = d_c / 50.0;
                printWriter.println(average);
            }
            printWriter.close();
        } 
        catch (FileNotFoundException e) 
        {
            e.getMessage();
        }
    }
}
