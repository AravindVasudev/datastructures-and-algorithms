import java.io.BufferedReader;
import java.io.InputStreamReader;

class ROBOGAME {
    public static void main(String[] args) throws Exception {
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(kb.readLine());

        while (testCases-- > 0) {
            String input = kb.readLine();
            int N = input.length();
            Robot[] robots = new Robot[N];

            for (int i = 0; i < N; i++) {
                if (input.charAt(i) == '.') continue;
                int offset = input.charAt(i) - '0';
                robots[i] = new Robot(i, Math.max(i - offset, 0), Math.min(i + offset, N - 1));
            }

            System.out.println(Robot.checkForCollision(robots) ? "unsafe" : "safe");
        }
    }

    private static class Robot {
        int pos, begin, end;

        Robot(int pos, int begin, int end) {
            this.pos = pos;
            this.begin = begin;
            this.end = end;
        }

        boolean doesCollide(Robot robot) {
            return (this.begin <= robot.end) && (robot.begin <= this.end);
        }

        static boolean checkForCollision(Robot[] robots) {
            for (int i = 0; i < robots.length - 1; i++) {
                if (robots[i] == null) continue;
                for (int j = i + 1; j < robots.length; j++) {
                    if (robots[j] == null) continue;

                    if (robots[i].doesCollide(robots[j])) {
                        return true;
                    }
                }
            }

            return false;
        }
    }
}
