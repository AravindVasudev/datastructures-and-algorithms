#include <fstream>
#include <iostream>
#include <vector>

const std::string XMAS{"XMAS"};

bool search(const std::vector<std::vector<char> >& grid, int row, int col,
            int x, int y, int next = 0) {
  // Not found.
  if (row < 0 || row >= grid.size() || col < 0 || col >= grid[0].size() ||
      grid[row][col] != XMAS[next]) {
    return false;
  }

  // Found.
  if (next == XMAS.size() - 1) {
    return true;
  }

  return search(grid, row + x, col + y, x, y, next+1);
}

int countXMASI(const std::vector<std::vector<char> >& grid) {
  const int N = grid.size();
  const int M = grid[0].size();
  int count{};

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      // Search all directions.
      for (int d1 = -1; d1 <= 1; d1++) {
        for (int d2 = -1; d2 <= 1; d2++) {
          if (d1 == 0 && d2 == 0) {
            continue;
          }

          if (search(grid, i, j, d1, d2)) {
            count++;
          }
        }
      }
    }
  }

  return count;
}

int countXMASII(std::vector<std::vector<char> >& grid) {
  const int N = grid.size();
  const int M = grid[0].size();
  const int START = 1;
  int count{};

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      // Search diagonals only.
      for (int d1 = -1; d1 <= 1; d1++) {
        for (int d2 = -1; d2 <= 1; d2++) {
          if (d1 == 0 || d2 == 0) {
            continue;
          }

          // If the current diagonal has 'MAS', search the other diagonal in
          // both possible directions.
          if (search(grid, i, j, d1, d2, START) &&
              (search(grid, i + (d1 * 2), j, (d1 * -1), d2, START) ||
               search(grid, i, j + (d2 * 2), d1, (d2 * -1), START))) {
            count++;
            grid[i + d1][j + d2] = '.';  // Mark visited.
          }
        }
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

  std::vector<std::vector<char> > grid;
  std::string line;
  while (std::getline(input, line)) {
    std::vector<char> row;
    for (char c : line) {
      row.push_back(c);
    }

    grid.emplace_back(row);
  }

  std::cout << "XMAS Count I: " << countXMASI(grid) << std::endl;
  std::cout << "XMAS Count II: " << countXMASII(grid) << std::endl;
}
