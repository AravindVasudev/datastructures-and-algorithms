import java.util.Scanner;

class SPAMCLAS {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int testCases = kb.nextInt();

        while (testCases-- > 0) {
            int N = kb.nextInt();
            int minX = kb.nextInt();
            int maxX = kb.nextInt();

            int w, b;
            int evenUser = 0, oddUser = 1;
            for (int i = 0; i < N; i++) {
                w = kb.nextInt();
                b = kb.nextInt();

                evenUser = w * evenUser + b;
                oddUser = w * oddUser + b;
            }

            int range = (maxX - minX + 1);
            int evenUsers = range / 2;
            int oddUsers = range - evenUsers;

            int spammers = 0;
            if ((evenUser & 1) == 1) spammers += evenUsers;
            if ((oddUser & 1) == 1) spammers += oddUsers;

            System.out.printf("%d %d\n", range - spammers, spammers);
        }
    }
}
