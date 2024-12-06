#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_set>

struct pairHash {
  inline std::size_t operator()(const std::pair<int, int>& p) const {
    return p.first * 130 + p.second;
  }
};

const std::vector<std::pair<int, int>> directions{
    {-1, 0}, {0, 1}, {1, 0}, {0, -1}};

std::pair<int, int> getCurrentPosition(const std::vector<std::string>& grid) {
  const int N = grid.size(), M = grid[0].size();

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (grid[i][j] == '^') {
        return {i, j};
      }
    }
  }

  throw "invalid grid";
}

inline int hashState(const std::pair<int, int>& p,
                             const std::pair<int, int>& d) {
  return (p.first * 130 + p.second) * 130 + (d.first * 10 + d.second);
}

std::unordered_set<std::pair<int, int>, pairHash> getDistinctPath(
    const std::vector<std::string>& grid, std::pair<int, int> position) {
  const int N = grid.size(), M = grid[0].size();
  int d = 0;
  std::unordered_set<std::pair<int, int>, pairHash> positions;
  positions.insert(position);

  // Brute force walk through the grid.
  while (true) {
    int nextX = position.first + directions[d].first;
    int nextY = position.second + directions[d].second;

    if (nextX < 0 || nextX >= N || nextY < 0 || nextY >= M) {
      break;  // left the grid.
    }

    if (grid[nextX][nextY] == '#') {
      d = (d + 1) % directions.size();  // turn right.
      continue;
    }

    position.first = nextX;
    position.second = nextY;
    positions.insert(position);
  }

  return positions;
}

bool doesLoop(const std::vector<std::string>& grid,
              std::pair<int, int> position) {
  const int N = grid.size(), M = grid[0].size();
  int d = 0;
  std::unordered_set<int> states;
  states.insert(hashState(position, directions[d]));

  // Brute force walk through the grid.
  while (true) {
    int nextX = position.first + directions[d].first;
    int nextY = position.second + directions[d].second;

    if (nextX < 0 || nextX >= N || nextY < 0 || nextY >= M) {
      break;  // left the grid.
    }

    if (grid[nextX][nextY] == '#') {
      d = (d + 1) % directions.size();  // turn right.
      continue;
    }

    position.first = nextX;
    position.second = nextY;

    const int state = hashState(position, directions[d]);
    if (states.find(state) != states.end()) {
      return true;  // loop
    }

    states.emplace(state);
  }

  return false;
}

int part1(std::vector<std::string>& grid, const std::pair<int, int>& position) {
  return getDistinctPath(grid, position).size();
}

int part2(std::vector<std::string>& grid, const std::pair<int, int>& position) {
  int count{};
  auto options = getDistinctPath(grid, position);

  for (const auto& option : options) {
    if (option.first == position.first && option.second == position.second) {
      continue;  // skip start.
    }

    grid[option.first][option.second] = '#';
    if (doesLoop(grid, position)) {
      count++;
    }
    grid[option.first][option.second] = '.';
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

  // Parse all the edges.
  while (getline(input, line)) {
    grid.emplace_back(line);
  }

  input.close();

  auto start = getCurrentPosition(grid);
  std::cout << "# of distinct positions: " << part1(grid, start) << std::endl;
  std::cout << "# of possibilites: " << part2(grid, start) << std::endl;
}
