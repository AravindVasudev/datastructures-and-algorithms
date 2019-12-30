class Solution {
    public String largestNumber(int[] nums) {
        Queue<String> q = new PriorityQueue<>(nums.length, (a, b) -> (b + a).compareTo(a + b));

        for (int n : nums) q.add(Integer.toString(n));

        if (q.peek().equals("0")) {
            return "0";
        }

        StringBuilder largest = new StringBuilder();
        while (!q.isEmpty()) largest.append(q.poll());

        return largest.toString();
    }
}
