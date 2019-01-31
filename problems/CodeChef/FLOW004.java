import java.io.BufferedReader;
import java.io.InputStreamReader;

class FLOW004 {
    public static void main(String[] args) throws Exception {
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(kb.readLine());

        while (testCases-- > 0) {
            String input = kb.readLine();
            System.out.println(input.charAt(0) + input.charAt(input.length() - 1) - 96); // '0' -> 48
        }
    }
}
