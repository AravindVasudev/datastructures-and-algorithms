import java.util.Scanner;

class FLOW002 {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int testCases = kb.nextInt();

        while (testCases-- > 0) {
            System.out.println(kb.nextInt() % kb.nextInt());
        }
    }
}
