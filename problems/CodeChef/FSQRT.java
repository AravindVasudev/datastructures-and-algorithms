import java.io.BufferedReader;
import java.io.InputStreamReader;

class FSQRT {
    public static void main(String[] args) throws Exception {
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(kb.readLine());

        while (testCases-- > 0) {
            System.out.println((int) Math.sqrt(Integer.parseInt(kb.readLine())));
        }
    }
}
