import java.util.*;

class TYPING {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int testcases = kb.nextInt();

        while (testcases-- > 0) {
            int N = kb.nextInt();
            Map<String, Integer> memo = new HashMap<>(N);

            int time = 0;
            while (N-- > 0) {
                String cur = kb.next();
                if (memo.containsKey(cur)) {
                    time += memo.get(cur) / 2;
                    continue;
                }

                int curTime = 2;
                boolean isCurLeft, isPrevLeft = isLeft(cur.charAt(0));
                for (int i = 1; i < cur.length(); i++) {
                    isCurLeft = isLeft(cur.charAt(i));
                    curTime += isCurLeft == isPrevLeft ? 4 : 2;

                    isPrevLeft = isCurLeft;
                }

                time += curTime;
                memo.put(cur, curTime);
            }

            System.out.println(time);
        }
    }

    private static boolean isLeft(char c) {
        return c == 'd' || c == 'f';
    }
}
