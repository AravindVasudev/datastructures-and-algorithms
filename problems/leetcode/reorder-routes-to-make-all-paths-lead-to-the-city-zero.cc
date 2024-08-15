// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        std::vector<std::vector<std::pair<int, int>>> graph(n);
        for (const auto& connection : connections) {
            graph[connection[0]].push_back({connection[1], 1});
            graph[connection[1]].push_back({connection[0], 0});
        }

        return dfs(graph);
    }

    int dfs(const std::vector<std::vector<std::pair<int, int>>>& graph, int node = 0, int parent = -1) {
        int count = 0;
        for (const auto& [neighbor, sign] : graph[node]) {
            if (neighbor != parent) {
                count += sign;
                count += dfs(graph, neighbor, node);
            }
        }

        return count;
    }
};
