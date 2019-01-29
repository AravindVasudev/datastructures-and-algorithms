import java.io.BufferedReader;
import java.io.InputStreamReader;

class WTCH {
    public static void main(String[] args) throws Exception {
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(kb.readLine());

        while (testCases-- > 0) {
            int N = Integer.parseInt(kb.readLine());
            String S = kb.readLine();

            int maxSecurities = 0, beg, subStrLen;
            for (int i = 0; i < N; i++) {
                if (S.charAt(i) == '0') {
                    beg = i;
                    while (i < N && S.charAt(i) == '0') i++;

                    subStrLen = i - beg;
                    if (i < N && S.charAt(i) == '1') subStrLen--;
                    if (beg > 0 && S.charAt(beg - 1) == '1') subStrLen--;

                    maxSecurities += (int) Math.ceil((subStrLen) / 2.0);
                }
            }

            System.out.println(maxSecurities);
        }
    }
}
