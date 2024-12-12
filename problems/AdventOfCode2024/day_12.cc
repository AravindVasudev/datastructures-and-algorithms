#include <format>
#include <fstream>
#include <iostream>
#include <vector>

const std::array<std::pair<int, int>, 4> directions{
    std::make_pair(-1, 0), std::make_pair(1, 0), std::make_pair(0, -1),
    std::make_pair(0, 1)};

class UnionFind {
 private:
  std::unordered_map<std::string, std::string> parent;

 public:
  int groups{};
  const std::string EMPTY = "";

  // Add a node.
  void add(std::string x) {
    if (parent.find(x) == parent.cend()) {
      parent[x] = x;
      groups++;
    }
  }

  // Find a node's parent.
  std::string find(std::string x) {
    if (parent.find(x) == parent.cend()) {
      return EMPTY;
    }

    while (x != parent[x]) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }

    return x;
  }

  // Union two nodes.
  void unite(std::string x, std::string y) {
    auto rootX = find(x), rootY = find(y);

    // Don't union if either of the node is not present.
    if (rootX == EMPTY || rootY == EMPTY) {
      return;
    }

    if (rootX != rootY) {
      groups--;
      parent[rootY] = rootX;
    }
  }
};

// Hash key for Union-Find.
inline std::string hash(const int i, const int j,
                        const std::pair<int, int>& d) {
  return std::format("{},{},{},{}", i, j, d.first, d.second);
}

std::pair<int, int> dfs(std::vector<std::string>& grid,
                        std::vector<std::vector<bool>>& visited, const int i,
                        const int j) {
  const int N = grid.size(), M = grid[0].size();
  visited[i][j] = true;

  std::pair<int, int> result{1, 0};
  for (auto& d : directions) {
    int nextI = i + d.first, nextJ = j + d.second;
    if (nextI < 0 || nextI >= N || nextJ < 0 || nextJ >= M ||
        grid[i][j] != grid[nextI][nextJ]) {
      result.second++;
      continue;
    } else if (!visited[nextI][nextJ]) {
      auto res = dfs(grid, visited, nextI, nextJ);
      result.first += res.first;
      result.second += res.second;
    }
  }

  return result;
}

int part1(std::vector<std::string>& grid) {
  const int N = grid.size(), M = grid[0].size();
  int cost{};
  std::vector<std::vector<bool>> visited(N, std::vector<bool>(M, false));

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (!visited[i][j]) {
        auto result = dfs(grid, visited, i, j);
        cost += result.first * result.second;
      }
    }
  }

  return cost;
}

int dfs2(std::vector<std::string>& grid,
         std::vector<std::vector<bool>>& visited, UnionFind& uf, const int i,
         const int j) {
  const int N = grid.size(), M = grid[0].size();
  visited[i][j] = true;

  int result{1};
  for (auto& d : directions) {
    int nextI = i + d.first, nextJ = j + d.second;
    if (nextI < 0 || nextI >= N || nextJ < 0 || nextJ >= M ||
        grid[i][j] != grid[nextI][nextJ]) {
      // Add the side.
      auto side = hash(nextI, nextJ, d);
      uf.add(side);

      // If any neighbor sides are present, union them.
      if (d.first == 0) {
        // This is a left or a right edge, union with top or bottom in the same
        // direction.
        uf.unite(hash(nextI + 1, nextJ, d), side);
        uf.unite(hash(nextI - 1, nextJ, d), side);
      } else {
        // This is a top or a bottom edge, union with left or right in the same
        // direction.
        uf.unite(hash(nextI, nextJ + 1, d), side);
        uf.unite(hash(nextI, nextJ - 1, d), side);
      }
    } else if (!visited[nextI][nextJ]) {
      result += dfs2(grid, visited, uf, nextI, nextJ);
    }
  }

  return result;
}

int part2(std::vector<std::string>& grid) {
  const int N = grid.size(), M = grid[0].size();
  int cost{};
  std::vector<std::vector<bool>> visited(N, std::vector<bool>(M, false));

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (!visited[i][j]) {
        UnionFind uf;
        auto result = dfs2(grid, visited, uf, i, j);
        cost += result * uf.groups;  // groups == sides.
      }
    }
  }

  return cost;
}

int main() {
  std::ifstream file("input.txt");
  if (!file.is_open()) {
    std::cerr << "Unable to open input.txt" << std::endl;
    return 1;
  }

  std::vector<std::string> grid;
  std::string line;

  while (std::getline(file, line)) {
    grid.emplace_back(line);
  }

  std::cout << "Part 1: " << part1(grid) << std::endl;
  std::cout << "Part 1: " << part2(grid) << std::endl;
}
