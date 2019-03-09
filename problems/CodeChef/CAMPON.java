import java.util.Scanner;

class CAMPON {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int testCases = kb.nextInt();

        while (testCases-- > 0) {
            int D = kb.nextInt();
            int[] d = new int[D];
            int[] p = new int[D];

            for (int i = 0; i < D; i++) {
                d[i] = kb.nextInt();
                p[i] = kb.nextInt();
            }

            int Q = kb.nextInt();
            int dead, req;
            for (int i = 0; i < Q; i++) {
                dead = kb.nextInt();
                req = kb.nextInt();

                int solved = 0;
                for (int j = 0; j < D; j++) {
                    if (d[j] <= dead) solved += p[j];
                }

                System.out.println("Go " + (solved >= req ? "Camp" : "Sleep"));
            }
        }
    }
}
