import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.awt.Point;

class AdaKing {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int testCases = kb.nextInt();

        for (int testCase = 0; testCase < testCases; testCase++) {
            Integer r = kb.nextInt();
            Integer c = kb.nextInt();
            int k = kb.nextInt();

            System.out.println(depthLimitedBFS(r, c, k));
            System.out.println(computeAsRectangle(r, c, k));
        }
    }

    private static int computeAsRectangle(int r, int c, int k) {
        int dx = Math.min(c + k, 8) - Math.max(c -  k, 1) + 1;
        int dy = Math.min(r + k, 8) - Math.max(r - k, 1) + 1;

        return dx * dy;
    }

    private static int depthLimitedBFS(int r, int c, int k) {
        HashSet<Point> visited = new HashSet<>();
        Queue<Point> q = new LinkedList<>();
        int curR, curC, count = 0;

        q.add(new Point(r, c));
        visited.add(new Point(r, c));
        while (!q.isEmpty()) {
            int levelSize = q.size();

            while (levelSize-- > 0) {
                Point cur = q.poll();
                count++;

                if (k == 0) continue;

                for (int i = -1; i <= 1; i++) {
                    for (int j = -1; j <= 1; j++) {
                        if (i == 0 && j == 0) continue;

                        Point next = new Point( cur.x + i, cur.y + j);

                        if (next.x < 1 || next.x > 8 || next.y < 1 || next.y > 8 || visited.contains(next)) {
                            continue;
                        }

                        q.add(next);
                        visited.add(next);
                    }
                }
            }

            k--;
        }

        return count;
    }
}