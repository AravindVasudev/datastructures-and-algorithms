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
    // return memo[key];
    return 0;
  }

  if (grid[loc.first][loc.second] == '^') {
    // std::cout << loc.first << " * " << loc.second << " = " << key << " | " << memo[key] << std::endl;
    return memo[key] = countSplits(grid, {loc.first, loc.second - 1}, memo) +
                countSplits(grid, {loc.first, loc.second + 1}, memo) + 1;
  }

  return memo[key] = countSplits(grid, {loc.first + 1, loc.second}, memo);
}

long countSplits(const std::vector<std::string>& grid,
                 const std::pair<size_t, size_t>& loc) {
  const auto X{grid.size()}, Y{grid[0].size()};
  std::vector<long> memo(X * Y, -1);

  return countSplits(grid, loc, memo);
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

  std::pair<size_t, size_t> start{0, findStart(grid[0])};

  std::cout << "Part 1: " << countSplits(grid, start) << std::endl;
  std::cout << "Part 2: " << "b" << std::endl;
}