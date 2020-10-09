// https://leetcode.com/problems/range-sum-query-mutable/
class NumArray {
    int[] tree;
    int n;
    
    private void buildTree(int[] nums, int treeIndex, int lo, int hi) {
        if (lo == hi) {
            tree[treeIndex] = nums[lo];
            return;
        }
        
        int mid = lo + (hi - lo) / 2;
        buildTree(nums, 2 * treeIndex + 1, lo, mid);
        buildTree(nums, 2 * treeIndex + 2, mid + 1, hi);
        
        tree[treeIndex] = tree[2 * treeIndex + 1] + tree[2 * treeIndex + 2];
    }
    
    private int queryInterval(int treeIndex, int lo, int hi, int i, int j) {
        if (lo > j || hi < i) {
            return 0;
        }
        
        if (i <= lo && j >= hi) {
            return tree[treeIndex];
        }
        
        int mid = lo + (hi - lo) / 2;
        
        if (j <= mid) {
            return queryInterval(2 * treeIndex + 1, lo, mid, i, j);
        } else if (i > mid) {
            return queryInterval(2 * treeIndex + 2, mid + 1, hi, i, j);
        }
        
        return queryInterval(2 * treeIndex + 1, lo, mid, i, j) +
            queryInterval(2 * treeIndex + 2, mid + 1, hi, i, j);
    }
    
    private void updateTree(int treeIndex, int lo, int hi, int i, int val) {
        if (lo == hi) {
            tree[treeIndex] = val;
            return;
        }
        
        int mid = lo + (hi - lo) / 2;
        
        if (i <= mid) {
            updateTree(2 * treeIndex + 1, lo, mid, i, val);
        } else {
            updateTree(2 * treeIndex + 2, mid + 1, hi, i, val);
        }
        
        tree[treeIndex] = tree[2 * treeIndex + 1] + tree[2 * treeIndex + 2];
    }

    public NumArray(int[] nums) {
        if (nums.length > 0) {
            n = nums.length - 1;
            tree = new int[nums.length * 4];
            buildTree(nums, 0, 0, nums.length - 1);
        }
    }
    
    public void update(int i, int val) {
        updateTree(0, 0, n, i, val);
    }
    
    public int sumRange(int i, int j) {
        return queryInterval(0, 0, n, i, j);
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */
