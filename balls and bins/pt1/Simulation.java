import java.security.SecureRandom;
import java.util.Arrays;

public class Simulation 
{
    public int[] simulate(int n) 
    {
        // 0: Bn, 1: Un, 2: Cn, 3: Dn, 4: Dn-Cn
        int[] results = new int[5];

        Arrays.fill(results, -1);

        int[] box = new int[n];

        int count = 0;
        int empty = n;
        int not_double = n;

        SecureRandom random = new SecureRandom();

        while (results[4] == -1) 
        {
            count++;
            int place = random.nextInt(n);
            box[place] += 1;

            switch (box[place])
            {
                case 1 : 
                    empty -= 1;
                    break;
                case 2 : 
                    not_double -= 1;
                    break;
                default:
                    break;
            }

            if (box[place] == 2 && results[0] == -1) 
            {
                results[0] = count;
            }

            if (n == count && results[1] == -1) 
            {
                results[1] = empty;
            }

            if (empty == 0 && results[2] == -1) 
            {
                results[2] = count;
            }

            if (not_double == 0 && results[3] == -1) 
            {
                results[3] = count;
                results[4] = results[3] - results[2];
            }
        }

        return results;
    }
}
