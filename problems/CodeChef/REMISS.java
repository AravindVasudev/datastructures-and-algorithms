import java.util.Scanner;

class REMISS {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int testCases = kb.nextInt();

        while (testCases-- > 0) {
            int A = kb.nextInt();
            int B = kb.nextInt();

            System.out.printf("%d %d\n", Math.max(A, B), A + B);
        }
    }
}
