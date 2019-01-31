import java.io.BufferedReader;
import java.io.InputStreamReader;

class FLOW006 {
    public static void main(String[] args) throws Exception {
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(kb.readLine());

        while (testCases-- > 0) {
            String input = kb.readLine();
            int sum = 0;
            for (int i = 0; i < input.length(); i++) {
                sum += input.charAt(i);
            }

            sum -= '0' * input.length();
            System.out.println(sum);
        }
    }
}
