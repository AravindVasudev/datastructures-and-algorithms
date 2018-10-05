import java.util.Scanner;

public class NumberOfSetBits {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        int nTestCases = kb.nextInt();
        for (int testCase = 0; testCase < nTestCases; testCase++) {
            int num = kb.nextInt();

            int counter = 0;
            while (num > 0) {
                num = num & (num - 1);
                counter++;
            }

            System.out.println(counter);
        }

    }
}
