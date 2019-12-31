// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to
class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        Map<Integer, Queue<Integer>> map = new HashMap<>();
        List<List<Integer>> output = new ArrayList<>();

        for (int i = 0; i < groupSizes.length; i++) {
            if (!map.containsKey(groupSizes[i])) {
                map.put(groupSizes[i], new LinkedList<>());
            }

            map.get(groupSizes[i]).add(i);
        }

        for (Map.Entry<Integer, Queue<Integer>> entry : map.entrySet()) {
            int curGroupSize = entry.getKey();
            Queue<Integer> members = entry.getValue();

            while (!members.isEmpty()) {
                List<Integer> curGroup = new ArrayList<>();

                for (int i = 0; i < curGroupSize && !members.isEmpty(); i++) {
                    curGroup.add(members.poll());
                }

                output.add(curGroup);
            }
        }

        return output;
    }
}
