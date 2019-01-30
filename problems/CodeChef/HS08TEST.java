import java.util.Scanner;

class HS08TEST {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        float X = kb.nextInt();
        float Y = kb.nextFloat();

        float balance = Y - X - 0.5f;
        System.out.printf("%.2f", (X % 5 != 0 || balance < 0) ? Y : balance);
    }
}