import java.util.Scanner;

class BITOBYT {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int testCases = kb .nextInt();

        while (testCases-- > 0) {
            int N = kb.nextInt() - 1;

            long bit = 1;
            long nibble = 0;
            long bite = 0;
            int bitCycle = 0, nibbleCycle = 0, biteCycle = 0;
            for (int i = 0; i < N; i++) {
                if (bit > 0) {
                    bitCycle++;
                    if (bitCycle >= 2) {
                        nibble += bit;
                        bit = 0;
                        bitCycle = 0;
                        nibbleCycle = 0;
                    }
                }

                if (nibble > 0) {
                    nibbleCycle++;
                    if (nibbleCycle > 8) {
                        bite += nibble;
                        nibble = 0;
                        nibbleCycle = 0;
                        biteCycle = 0;
                    }
                }

                if (bite > 0) {
                    biteCycle++;
                    if (biteCycle > 16) {
                        bit += bite * 2;
                        bite = 0;
                        biteCycle = 0;
                        bitCycle = 0;
                    }
                }
            }

            System.out.printf("%d %d %d\n", bit, nibble, bite);
        }
    }
}
