#include <fstream>
#include <iostream>

const char WALL = '#';
const char BOX = 'O';
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

void move(std::vector<std::string>& grid, const std::pair<int, int>& cell,
          const std::pair<int, int>& direction) {
  const int N = grid.size(), M = grid[0].size();

  // Find the first empty spot.
  std::pair<int, int> spot{cell.first + direction.first,
                           cell.second + direction.second};
  while (bounded(spot, N, M) && grid[spot.first][spot.second] == BOX) {
    spot.first += direction.first;
    spot.second += direction.second;
  }

  if (!bounded(spot, N, M) || grid[spot.first][spot.second] != EMPTY) {
    return;  // No empty spot.
  }

  // Bubble up all the boxes.
  while (spot.first != cell.first || spot.second != cell.second) {
    grid[spot.first][spot.second] = BOX;
    spot.first -= direction.first;
    spot.second -= direction.second;
    grid[spot.first][spot.second] = EMPTY;
  }
}

int computeTotalGPS(const std::vector<std::string>& grid) {
  const int N = grid.size(), M = grid[0].size();
  int gps{};

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (grid[i][j] == BOX) {
        gps += i * 100 + j;
      }
    }
  }

  return gps;
}

int part1(std::vector<std::string>& grid, std::string& input) {
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
    if (grid[next.first][next.second] == BOX) {
      move(grid, next, direction);
    }

    // Only go to the spot if empty.
    if (grid[next.first][next.second] == EMPTY) {
      robot = next;
    }
  }

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

  std::cout << "Part 1: " << part1(grid, input) << std::endl;
}
