import java.util.Scanner;

class CountDigits {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        String input = kb.next();
        int[] map = new int[10];
        for (int i = 0; i < input.length(); i++) {
            map[input.charAt(i) - '0']++;
        }

        for (int i = 0; i < 10; i++) {
            System.out.printf("%d %d\n", i, map[i]);
        }
    }
}
