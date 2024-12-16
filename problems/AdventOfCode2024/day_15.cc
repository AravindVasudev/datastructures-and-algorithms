#include <fstream>
#include <iostream>
#include <queue>

const char WALL = '#';
const char BOX = 'O';
const char BOX_L = '[';
const char BOX_R = ']';
const char EMPTY = '.';
const std::unordered_map<char, std::pair<int, int>> ACTIONS{
    {'<', {0, -1}}, {'>', {0, 1}}, {'^', {-1, 0}}, {'v', {1, 0}}};

std::pair<int, int> findRobot(const std::vector<std::string>& grid) {
  const int N = grid.size(), M = grid[0].size();
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (grid[i][j] == '@') {
        return {i, j};
      }
    }
  }

  throw "Invalid Input";
}

inline bool bounded(const std::pair<int, int>& cell, const int N, const int M) {
  return cell.first >= 0 && cell.first < N && cell.second >= 0 &&
         cell.second < M;
}

inline bool isBox(const char c) { return c == BOX || c == BOX_L || c == BOX_R; }

// Move one celled box.
void moveOne(std::vector<std::string>& grid, const std::pair<int, int>& cell,
             const std::pair<int, int>& direction) {
  const int N = grid.size(), M = grid[0].size();

  // Find the first empty spot.
  std::pair<int, int> spot{cell.first + direction.first,
                           cell.second + direction.second};
  while (bounded(spot, N, M) && isBox(grid[spot.first][spot.second])) {
    spot.first += direction.first;
    spot.second += direction.second;
  }

  if (!bounded(spot, N, M) || grid[spot.first][spot.second] != EMPTY) {
    return;  // No empty spot.
  }

  // Bubble up all the boxes.
  while (spot.first != cell.first || spot.second != cell.second) {
    grid[spot.first][spot.second] =
        grid[spot.first - direction.first][spot.second - direction.second];
    spot.first -= direction.first;
    spot.second -= direction.second;
    grid[spot.first][spot.second] = EMPTY;
  }
}

// Check if a two-celled box can move up or down.
bool canMove(const std::vector<std::string>& grid,
             const std::pair<int, int>& cell,
             const std::pair<int, int>& direction) {
  const int N = grid.size(), M = grid[0].size();
  if (!bounded(cell, N, M) || grid[cell.first][cell.second] == WALL) {
    return false;
  }

  if (grid[cell.first][cell.second] == EMPTY) {
    return true;
  }

  int offset = grid[cell.first][cell.second] == '[' ? 1 : -1;
  std::pair<int, int> cellNext{cell.first + direction.first,
                               cell.second + direction.second};
  std::pair<int, int> pairNext{cell.first + direction.first,
                               cell.second + direction.second + offset};

  // TODO: Add visited to cut repeated calls.
  return canMove(grid, cellNext, direction) &&
         canMove(grid, pairNext, direction);
}

// Move two-celled box up or down.
void move(std::vector<std::string>& grid, const std::pair<int, int>& cell,
          const std::pair<int, int>& direction) {
  if (grid[cell.first][cell.second] == EMPTY) {
    return;  // Base Case.
  }

  // Move the next row.
  int offset = grid[cell.first][cell.second] == '[' ? 1 : -1;
  std::pair<int, int> cellNext{cell.first + direction.first,
                               cell.second + direction.second};
  std::pair<int, int> pairNext{cell.first + direction.first,
                               cell.second + direction.second + offset};

  move(grid, cellNext, direction);
  move(grid, pairNext, direction);

  // Move the current row.
  grid[cellNext.first][cellNext.second] = grid[cell.first][cell.second];
  grid[pairNext.first][pairNext.second] =
      grid[cell.first][cell.second + offset];
  grid[cell.first][cell.second] = grid[cell.first][cell.second + offset] =
      EMPTY;
}

// Move two cell box stack up or down.
void moveTwo(std::vector<std::string>& grid, const std::pair<int, int>& cell,
             const std::pair<int, int>& direction) {
  const int N = grid.size(), M = grid[0].size();
  // Check if the stack is movable.
  if (!canMove(grid, cell, direction)) {
    return;
  }

  move(grid, cell, direction);
}

int computeTotalGPS(const std::vector<std::string>& grid) {
  const int N = grid.size(), M = grid[0].size();
  int gps{};

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (grid[i][j] == BOX || grid[i][j] == BOX_L) {
        gps += i * 100 + j;
      }
    }
  }

  return gps;
}

// Execute input tape.
void execute(std::vector<std::string>& grid, const std::string& input) {
  const int N = grid.size(), M = grid[0].size();
  auto robot = findRobot(grid);
  grid[robot.first][robot.second] = EMPTY;  // Remove robot from grid.

  for (char action : input) {
    const auto& direction = ACTIONS.at(action);
    std::pair<int, int> next{robot.first + direction.first,
                             robot.second + direction.second};

    if (!bounded(next, N, M) || grid[next.first][next.second] == WALL) {
      continue;  // Cannot move to next.
    }

    // Move if there are boxes.
    if (grid[next.first][next.second] == BOX_L ||
        grid[next.first][next.second] == BOX_R) {
      if (direction.first == 0) {
        moveOne(grid, next, direction);
      } else {
        moveTwo(grid, next, direction);
      }
    } else if (grid[next.first][next.second] == BOX) {
      moveOne(grid, next, direction);
    }

    // Only go to the spot if empty.
    if (grid[next.first][next.second] == EMPTY) {
      robot = next;
    }
  }
}

std::vector<std::string> scaleGrid(const std::vector<std::string>& grid) {
  std::vector<std::string> scaled;

  for (auto& line : grid) {
    std::string updated;
    for (char c : line) {
      switch (c) {
        case WALL:
          updated += "##";
          break;
        case BOX:
          updated += "[]";
          break;
        case EMPTY:
          updated += "..";
          break;
        case '@':
          updated += "@.";
          break;
      }
    }

    scaled.emplace_back(updated);
  }

  return scaled;
}

int GPSWithInput(std::vector<std::string>& grid, const std::string& input) {
  execute(grid, input);
  return computeTotalGPS(grid);
}

int main() {
  std::ifstream file("input.txt");
  if (!file.is_open()) {
    std::cerr << "Unable to open input.txt" << std::endl;
    return 1;
  }

  std::vector<std::string> grid;
  std::string input;
  std::string line;

  while (std::getline(file, line)) {
    if (line.empty()) {
      break;
    }

    grid.emplace_back(line);
  }

  while (std::getline(file, line)) {
    input += line;
  }

  auto scaled = scaleGrid(grid);
  std::cout << "Part 1: " << GPSWithInput(grid, input) << std::endl;
  std::cout << "Part 2: " << GPSWithInput(scaled, input) << std::endl;
}
