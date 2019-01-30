import java.io.BufferedReader;
import java.io.InputStreamReader;

class FLOW007 {
    public static void main(String[] args) throws Exception {
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(kb.readLine());

        while (testCases-- > 0) {
            int input = Integer.parseInt(kb.readLine());
            int rev = 0;
            while (input > 0) {
                rev = (rev * 10) + (input % 10);
                input /= 10;
            }

            System.out.println(rev);
        }
    }
}
