import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

class QUALPREL {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int testCases = kb.nextInt();

        while (testCases-- > 0) {
            int N = kb.nextInt();
            int K = kb.nextInt();

            Integer[] S= new Integer[N];
            for (int i = 0; i < N; i++) {
                S[i] = kb.nextInt();
            }

            Arrays.sort(S, Collections.reverseOrder());


            int qualifiedTeams = K, kVal = S[K - 1];
            for (int i = K; i < N; i++) {
                if (S[i] != kVal) break;
                qualifiedTeams++;
            }

            System.out.println(qualifiedTeams);
        }
    }
}
