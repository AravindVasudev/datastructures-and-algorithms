import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

// https://www.codechef.com/problems/FANCY
class FANCY {
    public static void main(String[] args) throws IOException {
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(kb.readLine());
        StringBuilder output = new StringBuilder();

        while (testCases-- > 0) {
            String input = kb.readLine();

            output.append(Arrays.asList(input.split(" ")).contains("not") ? "Real Fancy\n" : "regularly fancy\n");
        }

        System.out.print(output);
    }
}
