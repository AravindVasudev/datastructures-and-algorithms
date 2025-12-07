#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

size_t findStart(const std::string& firstRow) {
  const auto size = firstRow.size();
  for (auto i = 0; i < size; i++) {
    if (firstRow[i] == 'S') {
      return i;
    }
  }

  throw "Not found";
}

long countSplits(const std::vector<std::string>& grid,
                 const std::pair<size_t, size_t>& loc, std::vector<long>& memo) {
  // Out-Of-Bound.
  const auto X{grid.size()}, Y{grid[0].size()};
  if (loc.first < 0 || loc.first >= X || loc.second < 0 || loc.second >= Y) {
    return 0;
  }

  auto key = loc.first * Y + loc.second;
  if (memo[key] != -1) {
    return memo[key];
  }

  if (grid[loc.first][loc.second] == '^') {
    return memo[key] = countSplits(grid, {loc.first, loc.second - 1}, memo) +
                countSplits(grid, {loc.first, loc.second + 1}, memo) + 1;
  }

  return memo[key] = countSplits(grid, {loc.first + 1, loc.second}, memo);
}

std::pair<long, long> countSplits(const std::vector<std::string>& grid) {
  const auto X{grid.size()}, Y{grid[0].size()};
  const std::pair<size_t, size_t> start{0, findStart(grid[0])};
  std::vector<long> memo(X * Y, -1);

  // Include current timeline.
  auto timelines = countSplits(grid, start, memo) + 1;

  // Count activated splitters.
  long splits{};
  for (int i = 0; i < X; i++) {
    for (int j = 0; j < Y; j++) {
      if (grid[i][j] == '^' && memo[i * Y + j] != -1) {
        splits++;
      }
    }
  }

  return {splits, timelines};
}

int main() {
  std::ifstream input("input.txt");
  if (!input.is_open()) {
    std::cerr << "Error: Unable to open input.txt" << std::endl;
    return 1;
  }

  std::vector<std::string> grid;
  std::string line;
  while (std::getline(input, line)) {
    grid.push_back(line);
  }

  const auto [splits, timelines] = countSplits(grid);
  std::cout << "Part 1: " << splits << std::endl;
  std::cout << "Part 2: " << timelines << std::endl;
}