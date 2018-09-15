import java.util.Scanner;

// https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/monk-visits-coderland-4/
public class MonkVisitsCoderland {
    private static long calculateMinCost(long[] cost, long[] required) {
        int i = 0, j = 0;
        long totalCost = 0;

        while (j < cost.length) {
            if (cost[j] < cost[i]) {
                i = j;
                continue;
            }

            totalCost += cost[i] * required[j++];
        }

        return totalCost;
    }


    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        int nTestCases = kb.nextInt();
        for (int testCase = 0; testCase < nTestCases; testCase++) {
            int nCheckpoints = kb.nextInt();
            long[] cost = new long[nCheckpoints];
            long[] required = new long[nCheckpoints];

            for (int i = 0; i < nCheckpoints; i++) {
                cost[i] = kb.nextLong();
            }

            for (int i = 0; i < nCheckpoints; i++) {
                required[i] = kb.nextLong();
            }

            System.out.println(calculateMinCost(cost, required));
        }
    }
}

