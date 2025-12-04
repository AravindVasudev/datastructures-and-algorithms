#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

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
    }
  }

  return paperCount < 4;
}

long part1(const std::vector<std::string>& grid) {
  long canMove{};
  auto X{grid.size()}, Y{grid[0].size()};

  for (auto i = 0; i < X; i++) {
    for (auto j = 0; j < Y; j++) {
      // Check if the cell can be accessed.
      if (grid[i][j] == PAPER && canAccess(grid, i, j)) {
        canMove++;
      }
    }
  }

  return canMove;
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
  std::cout << "Part 2: " << "b" << std::endl;
}