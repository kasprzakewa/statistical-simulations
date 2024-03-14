import java.security.SecureRandom;

public class Simulation 
{
    public int simulate(int n, int d) 
    {
        int[] box = new int[n];

        int count = 0;
        int max_place = 0;
        int temp;
        int place;

        SecureRandom random = new SecureRandom();

        while (count < n) 
        {
            place = -1;
            count++;

            for(int i = 0; i < d; i++)
            {
                temp = random.nextInt(n);
                if(place == -1 || box[temp] < box[place])
                    place = temp;
            }

            box[place] += 1;

            if (box[place] > box[max_place])
            {
                max_place = place;
            } 
        }

        return box[max_place];
    }
}
