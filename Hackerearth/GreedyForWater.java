import java.util.Arrays;
import java.util.Scanner;

public class GreedyForWater {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int testCases = kb.nextInt();

        for (int testCase = 0; testCase < testCases; testCase++) {
            int n = kb.nextInt();
            int x = kb.nextInt();

            int[] capacities = new int[n];
            for (int i = 0; i < n; i++) {
                capacities[i] = kb.nextInt();
            }

            Arrays.sort(capacities);

            int maxBottles = 0;
            for (int i = 0; i < n && capacities[i] < x; maxBottles++, x-=capacities[i], i++);

            System.out.println(maxBottles);
        }
    }
}
