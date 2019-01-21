import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

// https://www.codechef.com/problems/ADASCOOL
class ADASCOOL {
    private static HashSet<Point> adjecents = new HashSet<>();

    static {
        adjecents.add(new Point(-1, 0));
        adjecents.add(new Point(0, -1));
        adjecents.add(new Point(0, 1));
        adjecents.add(new Point(1, 0));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(kb.readLine());
        StringBuilder output = new StringBuilder();

        while (testCases-- > 0) {
            String[] input = kb.readLine().trim().split(" ");
            int N = Integer.parseInt(input[0]);
            int M = Integer.parseInt(input[1]);

//            output.append(backTracking(N, M) ? "YES\n" : "NO\n"); // Naive using backtracking
            output.append(((N * M) & 1) == 0 ? "YES\n" : "NO\n"); // N * M should be even
        }

        System.out.print(output);
    }



    private static boolean backTracking(int N, int M) {
        boolean[][] occupied = new boolean[N][M];

        return isShufflePossible(occupied, new Point(0, 0));
    }

    private static boolean isShufflePossible(boolean[][] occupied, Point curCell) {
        for (Point curDir : adjecents) {
            Point cur = new Point(curCell.x + curDir.x, curCell.y + curDir.y);

            if (cur.x < 0 || cur.x > occupied.length - 1 || cur.y < 0 || cur.y > occupied[0].length - 1
                    || occupied[cur.x][cur.y]) {
                continue;
            }

            Point next = getNextCell(curCell, occupied.length, occupied[0].length);
            if (next == null) return true;

            occupied[cur.x][cur.y] = true;
            if (isShufflePossible(occupied, next)) {
                return true;
            }

            occupied[cur.x][cur.y] = false;
        }

        return false;
    }

    private static Point getNextCell(Point cur, int N, int M) {
        if (cur.y + 1 < M) {
            return new Point(cur.x, cur.y + 1);
        }

        if (cur.x + 1 < N) {
            return new Point(cur.x + 1, 0);
        }

        return null;
    }
}
