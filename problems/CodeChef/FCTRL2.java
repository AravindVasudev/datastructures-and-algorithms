import java.math.BigInteger;
import java.util.Scanner;

class FCTRL2 {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int testCases = kb.nextInt();

        while (testCases-- > 0) {
            int n = kb.nextInt();
            BigInteger fact = new BigInteger("1");

            while (n > 1) fact = fact.multiply(BigInteger.valueOf(n--));
            System.out.println(fact);
        }
    }
}
