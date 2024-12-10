#include <fstream>
#include <iostream>
#include <unordered_set>

const std::vector<std::pair<int, int>> directions = {
    {-1, 0}, {1, 0}, {0, -1}, {0, 1}};

inline int hash(int i, int j) { return i * 1000 + j; }

int countTrails(const std::vector<std::string>& grid, const int i, const int j,
                std::unordered_set<int>& visited) {
  const int N = grid.size(), M = grid[0].size();
  if (grid[i][j] == '9') {
    visited.emplace(hash(i, j));
    return 1;
  }

  int paths{};
  for (const auto& d : directions) {
    int nextI = i + d.first, nextJ = j + d.second;
    if (nextI < 0 || nextI >= N || nextJ < 0 || nextJ >= M ||
        (grid[nextI][nextJ] - grid[i][j]) != 1 ||
        visited.find(hash(nextI, nextJ)) != visited.end()) {
      continue;
    }

    paths += countTrails(grid, nextI, nextJ, visited);
  }

  return paths;
}

int part1(const std::vector<std::string>& grid) {
  const int N = grid.size(), M = grid[0].size();
  int count{};

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (grid[i][j] == '0') {  // Trail head.
        std::unordered_set<int> visited;
        count += countTrails(grid, i, j, visited);
      }
    }
  }

  return count;
}

int countRatings(const std::vector<std::string>& grid, const int i,
                 const int j) {
  const int N = grid.size(), M = grid[0].size();
  if (grid[i][j] == '9') {
    return 1;
  }

  int paths{};
  for (const auto& d : directions) {
    int nextI = i + d.first, nextJ = j + d.second;
    if (nextI < 0 || nextI >= N || nextJ < 0 || nextJ >= M ||
        (grid[nextI][nextJ] - grid[i][j]) != 1) {
      continue;
    }

    paths += countRatings(grid, nextI, nextJ);
  }

  return paths;
}

int part2(std::vector<std::string>& grid) {
  const int N = grid.size(), M = grid[0].size();
  int count{};

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (grid[i][j] == '0') {  // Trail head.
        count += countRatings(grid, i, j);
      }
    }
  }

  return count;
}

int main() {
  std::ifstream input("input.txt");
  if (!input.is_open()) {
    std::cerr << "Error: Unable to open input.txt" << std::endl;
    return 1;
  }

  std::vector<std::string> grid;
  std::string line;
  while (getline(input, line)) {
    grid.emplace_back(line);
  }

  input.close();

  std::cout << "Part 1: " << part1(grid) << std::endl;
  std::cout << "Part 2: " << part2(grid) << std::endl;
}
