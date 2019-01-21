import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// https://www.codechef.com/problems/XORNEY
class XORNEY {
    public static void main(String[] args) throws IOException {
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(kb.readLine());
        StringBuilder output = new StringBuilder();

        while (testCases-- > 0) {
            String[] input = kb.readLine().trim().split(" ");
            long L = Long.parseLong(input[0]);
            long R = Long.parseLong(input[1]);

            long count = (R - L) / 2;
            if ((L & 1) == 1 || (R & 1) == 1) count++;
            output.append((count & 1) == 1 ? "Odd\n" : "Even\n");
        }

        System.out.print(output);
    }
}
