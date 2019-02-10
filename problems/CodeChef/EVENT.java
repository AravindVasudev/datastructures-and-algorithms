import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class EVENT {
    public static void main(String[] args) {
        Map<String, Integer> days = new HashMap<>();

        days.put("monday", 1);
        days.put("tuesday", 2);
        days.put("wednesday", 3);
        days.put("thursday", 4);
        days.put("friday", 5);
        days.put("saturday", 6);
        days.put("sunday", 7);

        Scanner kb = new Scanner(System.in);
        int testCases = kb.nextInt();

        while (testCases-- > 0) {
            int S = days.get(kb.next());
            int E = days.get(kb.next());
            int L = kb.nextInt();
            int R = kb.nextInt();

            System.out.println(getDuration(S, E, L, R));
        }
    }

    private static String getDuration(int S, int E, int L, int R) {
        int distance = (E - S + 7) % 7 + 1;
        int count = 0;
        int num = 0;

        while (L <= R) {
            if ((L - distance) % 7 == 0) {
                count++;
                num = L;

                break;
            }

            L++;
        }

        if ((L + 7) <= R) count++;

        return count == 0 ? "impossible" : (count == 1 ? Integer.toString(num) : "many");
    }
}