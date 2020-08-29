public class URLify {
    public static void urlify(char[] url, int length) {
        int end = url.length - 1;
        for (int i = length - 1; i >= 0; i--) {
            if (url[i] == ' ') {
                url[end--] = '0';
                url[end--] = '2';
                url[end--] = '%';
            } else {
                url[end--] = url[i];
            }
        }
    }

    public static void main(String[] args) {
        char[] testCase1 = "Mr John Smith    ".toCharArray();
        int testCaseLen1 = 13;

        urlify(testCase1, testCaseLen1);
        System.out.printf("--%s--", new String(testCase1));
    }
}
