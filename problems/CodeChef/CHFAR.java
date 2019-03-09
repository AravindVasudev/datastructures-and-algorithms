import java.util.Scanner;

class CHFAR {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int testCases = kb.nextInt();

        while (testCases-- > 0) {
            int N = kb.nextInt();
            int K = kb.nextInt();

            int count = 0;
            for (int i = 0; i < N; i++) {
                if (kb.nextInt() > 1) {
                    count++;
                }
            }

            System.out.println(count <= K ? "YES" : "NO");
        }
    }
}
