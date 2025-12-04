#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

struct pairHash {
  inline std::size_t operator()(const std::pair<size_t, size_t>& p) const {
    return p.first ^ (p.second << 1);
  }
};

const char EMPTY = '.';
const char PAPER = '@';

bool canAccess(const std::vector<std::string>& grid, size_t i, size_t j) {
  int paperCount{};
  auto X{grid.size()}, Y{grid[0].size()};

  for (int offsetI = -1; offsetI <= 1; offsetI++) {
    for (int offsetJ = -1; offsetJ <= 1; offsetJ++) {
      // Just check the eight surrounding cells.
      if (offsetI == 0 && offsetJ == 0) {
        continue;
      }

      auto nextI = i + offsetI;
      auto nextJ = j + offsetJ;

      // Out of bound.
      if (nextI < 0 || nextI >= X || nextJ < 0 || nextJ >= Y) {
        continue;
      }

      if (grid[nextI][nextJ] == PAPER) {
        paperCount++;
      }

      // No need to check more.
      if (paperCount >= 4) {
        return false;
      }
    }
  }

  return paperCount < 4;
}

std::unordered_set<std::pair<size_t, size_t>, pairHash> findCellsToRemove(
    const std::vector<std::string>& grid) {
  auto X{grid.size()}, Y{grid[0].size()};
  std::unordered_set<std::pair<size_t, size_t>, pairHash> toRemove;

  for (auto i = 0; i < X; i++) {
    for (auto j = 0; j < Y; j++) {
      // Check if the cell can be accessed.
      if (grid[i][j] == PAPER && canAccess(grid, i, j)) {
        toRemove.insert({i, j});
      }
    }
  }

  return toRemove;
}

long part1(const std::vector<std::string>& grid) {
  return findCellsToRemove(grid).size();
}

long part2(std::vector<std::string>& grid) {
  long boxesMoved{};

  while (true) {
    const auto toRemove = findCellsToRemove(grid);

    // Stop when there is nothing to remove.
    if (toRemove.empty()) {
      break;
    }

    for (auto& index : toRemove) {
      grid[index.first][index.second] = EMPTY;
      boxesMoved++;
    }
  }

  return boxesMoved;
}

int main() {
  std::ifstream input("input.txt");
  if (!input.is_open()) {
    std::cerr << "Error: Unable to open input.txt" << std::endl;
    return 1;
  }

  std::string line;
  std::vector<std::string> grid;
  while (std::getline(input, line)) {
    grid.push_back(line);
  }

  std::cout << "Part 1: " << part1(grid) << std::endl;
  std::cout << "Part 2: " << part2(grid) << std::endl;
}