import java.util.Arrays;
import java.util.Scanner;

class FLOW017 {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int testCases = kb.nextInt();
        int[] arr = new int[3];

        while (testCases-- > 0) {
            for (int i = 0; i < 3; i++) arr[i] = kb.nextInt();
            Arrays.sort(arr);

            System.out.println(arr[1]);
        }
    }
}
