import java.awt.Point;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class KCHESS {
    public static void main(String[] args) throws Exception {
        Scanner kb = new Scanner(System.in);
        int testCases = kb.nextInt();
        int[] move1 = new int[]{-1, 1};
        int[] move2 = new int[]{-2, 2};

        while (testCases-- > 0) {
            int nKnights = kb.nextInt();
            Point[] knights = new Point[nKnights];

            for (int i = 0; i < nKnights; i++) {
                knights[i] = new Point(kb.nextInt(), kb.nextInt());
            }

            Point king = new Point(kb.nextInt(), kb.nextInt());
            Map<Point, Boolean> hitMap = new HashMap<>(9);
            for (int i = -1; i <= 1; i++) {
                for (int j = -1; j <= 1; j++) {
                    hitMap.put(new Point(king.x + i, king.y + j), false);
                }
            }

            for (int i = 0; i < nKnights; i++) {
                for (int m1 = 0; m1 < 2; m1++) {
                    for (int m2 = 0; m2 < 2; m2++) {
                        Point curKnightMove1 = new Point(knights[i].x + move1[m1], knights[i].y + move2[m2]);
                        Point curKnightMove2 = new Point(knights[i].x + move2[m1], knights[i].y + move1[m2]);

                        if (hitMap.containsKey(curKnightMove1)) {
                            hitMap.put(curKnightMove1, true);
                        }

                        if (hitMap.containsKey(curKnightMove2)) {
                            hitMap.put(curKnightMove2, true);
                        }
                    }
                }
            }

            Boolean isCheckmate = true;
            for (Boolean isHit : hitMap.values()) {
                isCheckmate &= isHit;
            }

            System.out.println(isCheckmate ? "YES" : "NO");
        }
    }
}
