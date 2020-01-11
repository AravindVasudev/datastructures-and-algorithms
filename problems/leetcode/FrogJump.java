class Solution {
    public boolean canCross(int[] stones) {
        Set<Integer>[] table = new Set[stones.length];
        int lastStone = stones[stones.length - 1];

        List<Integer> stonesList = new ArrayList<>(stones.length);
        for (int stone : stones) {
            stonesList.add(stone);
        }

        // First Jump
        int pos = stonesList.indexOf(stones[0] + 1);
        if (pos == -1) {
            return false;
        }

        table[pos] = new HashSet<>();
        table[pos].add(1);

        for (int i = 1; i < stones.length; i++) {
            if (table[i] == null) {
                continue;
            }

            for (int step : table[i]) {
                for (int j = step - 1; j <= step + 1; j++) {
                    if (j <= 0) {
                        continue;
                    }

                    Integer next = stones[i] + j;
                    if (lastStone == next) {
                        return true;
                    }

                    int index = stonesList.indexOf(next);
                    if (index == -1) {
                        continue;
                    }


                    if (table[index] == null) {
                        table[index] = new HashSet<>();
                    }

                    table[index].add(j);
                }
            }
        }

        return table[table.length - 1] != null;
    }
}
