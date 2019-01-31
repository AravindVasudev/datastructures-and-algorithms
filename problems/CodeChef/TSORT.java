import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

class TSORT {
    public static void main(String[] args) throws Exception {
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(kb.readLine());
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) arr[i] = Integer.parseInt(kb.readLine());
        Arrays.sort(arr);
        for (int i = 0; i < N; i++) System.out.println(arr[i]);
    }
}
