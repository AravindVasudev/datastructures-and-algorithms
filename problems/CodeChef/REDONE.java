import java.util.Scanner;

class REDONE {
    private static long MOD = 1000000007;
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int testCases = kb.nextInt();

        long[] answers = new long[1000000];
        long cur = 1;
        answers[0] = 1;
        for (int i = 2; i <= 1000000; i++) {
            answers[i - 1] = cur = (cur + i + cur * i) % MOD;
        }

        while (testCases-- > 0) {
            int N = kb.nextInt();

            System.out.println(answers[N - 1]);
        }
    }
}
