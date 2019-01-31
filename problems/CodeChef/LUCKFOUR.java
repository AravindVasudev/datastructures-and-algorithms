import java.io.BufferedReader;
import java.io.InputStreamReader;

class LUCKFOUR {
    public static void main(String[] args) throws Exception {
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(kb.readLine());

        while (testCases-- > 0) {
            String input = kb.readLine();
            int count = 0;
            for (int i = 0; i < input.length(); i++) {
                if (input.charAt(i) == '4') count++;
            }

            System.out.println(count);
        }
    }
}
