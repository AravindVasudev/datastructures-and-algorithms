import java.util.Scanner;

class TLG {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int N = kb.nextInt();

        boolean winner = false; // true -> P1
        int P1 = 0, P2 = 0, maxScoreDiff = -1;
        while (N-- > 0) {
            P1 += kb.nextInt();
            P2 += kb.nextInt();

            int scoreDiff = Math.abs(P1 - P2);
            if (scoreDiff > maxScoreDiff) {
                maxScoreDiff = scoreDiff;
                winner = P1 > P2;
            }
        }

        System.out.printf("%d %d", winner ? 1 : 2, maxScoreDiff);
    }
}
