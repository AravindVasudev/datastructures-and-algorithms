#include <fstream>
#include <iostream>
#include <vector>

bool search(const std::vector<std::vector<char> >& grid, int row, int col,
            int x, int y, char next = 'X') {
  // Not found.
  if (row < 0 || row >= grid.size() || col < 0 || col >= grid[0].size() ||
      grid[row][col] != next) {
    return false;
  }

  // Found.
  if (next == 'S') {
    return true;
  }

  switch (next) {
    case 'X':
      next = 'M';
      break;
    case 'M':
      next = 'A';
      break;
    case 'A':
      next = 'S';
      break;
  }

  return search(grid, row + x, col + y, x, y, next);
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
  const char START = 'M';
  int count{};

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      // Case 1: Top Left.
      if (search(grid, i, j, -1, -1, START) &&
          (search(grid, i - 2, j, 1, -1, START) ||
           search(grid, i, j - 2, -1, 1, START))) {
        count++;
        grid[i - 1][j - 1] = '.';  // Mark visited.
      }

      // Case 2: Top Right.
      if (search(grid, i, j, -1, 1, START) &&
          (search(grid, i - 2, j, 1, 1, START) ||
           search(grid, i, j + 2, -1, -1, START))) {
        count++;
        grid[i - 1][j + 1] = '.';  // Mark visited.
      }

      // Case 3: Bottom Left.
      if (search(grid, i, j, 1, -1, START) &&
          (search(grid, i + 2, j, -1, -1, START) ||
           search(grid, i, j - 2, 1, 1, START))) {
        count++;
        grid[i + 1][j - 1] = '.';  // Mark visited.
      }

      // Case 4: Bottom Right.
      if (search(grid, i, j, 1, 1, START) &&
          (search(grid, i + 2, j, -1, 1, START) ||
           search(grid, i, j + 2, 1, -1, START))) {
        count++;
        grid[i + 1][j + 1] = '.';  // Mark visited.
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
