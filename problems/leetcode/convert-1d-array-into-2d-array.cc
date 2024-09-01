// https://leetcode.com/problems/convert-1d-array-into-2d-array/
class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        if (m * n != original.size()) {
            return {};
        }

        vector<vector<int>> reconstructed(m, std::vector<int>(n));
        int idx = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                reconstructed[i][j] = original[idx++];
            }
        }

        return reconstructed;
    }
};
