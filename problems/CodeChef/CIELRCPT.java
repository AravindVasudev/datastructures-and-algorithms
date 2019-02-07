import java.util.Scanner;

class CIELRCPT {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int testCases = kb.nextInt();

        int[] menu = new int[12];
        for (int i = 0; i < 12; i++) menu[i] = (1 << i);
        while (testCases-- > 0) {
            int N = kb.nextInt();

            int items = 0;
            for (int i = 11; i >=0; i--) {
                items += N / menu[i];
                N %= menu[i];
            }

            System.out.println(items);
        }
    }
}