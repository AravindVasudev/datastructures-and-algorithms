import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class H1 {
    public static void main(String[] args) throws Exception {
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(kb.readLine());
        StringBuilder output = new StringBuilder();

        Map<String, Integer> stateVsDistance = generateAllStates();
        while (testCases-- > 0) {
            kb.readLine();
            StringBuilder query = new StringBuilder();
            for (int i = 0; i < 3; i++) {
                query.append(kb.readLine().replace(" ", ""));
            }

            output.append(stateVsDistance.getOrDefault(query.toString(), -1));
            output.append("\n");
        }

        System.out.print(output);
    }

    private static Map<String, Integer> generateAllStates() {
        Map<String, Integer> stateVsDistance = new HashMap<>();
        int[][] nexts = new int[][]{{0, 1}, {1, 0}};

        Queue<String> q = new LinkedList<>();
        q.add("123456789");
        stateVsDistance.put("123456789", 0);

        int cur, next;
        while (!q.isEmpty()) {
            String curState = q.poll();

            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    cur = i * 3 + j;
                    for (int n = 0; n <= 1; n++) {
                        next = (i + nexts[n][0]) * 3 + (j + nexts[n][1]);

                        if ((i + nexts[n][0]) < 3 && (j + nexts[n][1]) < 3 && canSwap(curState.charAt(cur), curState.charAt(next))) {
                            char[] newState = curState.toCharArray();
                            char temp = newState[cur];
                            newState[cur] = newState[next];
                            newState[next] = temp;

                            String newStateStr = new String(newState);
                            if (!stateVsDistance.containsKey(newStateStr)) {
                                stateVsDistance.put(newStateStr, stateVsDistance.get(curState) + 1);
                                q.add(newStateStr);
                            }
                        }
                    }
                }
            }
        }

        return stateVsDistance;
    }

    private static boolean canSwap(char a, char b) {
        int sum = a + b - 96; // '0' = 48
        return (sum == 3 || sum == 5 || sum == 7 || sum == 11 || sum == 13 || sum == 17);
    }
}