import java.util.Scanner;

class INTEST {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int N = kb.nextInt();
        int K = kb.nextInt();

        int count = 0;
        while (N-- > 0) {
            if (kb.nextInt() % K == 0) count++;
        }

        System.out.println(count);
    }
}
