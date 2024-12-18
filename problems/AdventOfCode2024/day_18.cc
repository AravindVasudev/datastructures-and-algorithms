#include <fstream>
#include <iostream>
#include <queue>
#include <unordered_set>

const int N = 71;        // Dimension
const int FALLEN = 1024;  // Fallen for Part-1.
const char WALL = '#';
const std::array<std::pair<int, int>, 4> directions{
    std::make_pair(-1, 0),
    std::make_pair(0, 1),
    std::make_pair(1, 0),
    std::make_pair(0, -1),
};

struct pairHash {
  inline std::size_t operator()(const std::pair<int, int>& p) const {
    return p.first ^ (p.second << 1);
  }
};

void addWall(std::vector<std::string>& grid, const std::string& line) {
  auto it = line.find(',');
  const int X = std::stoi(line.substr(0, it)),
            Y = std::stoi(line.substr(it + 1));
  grid[Y][X] = WALL;
}

int part1(const std::vector<std::string>& fallingOrder) {
  // Setup grid.
  std::vector<std::string> grid(N, std::string(N, '.'));
  for (int i = 0; i < FALLEN; i++) {
    addWall(grid, fallingOrder[i]);
  }

  std::cout << std::endl;
  for (auto& s : grid) std::cout << s << std::endl;

  std::queue<std::pair<int, int>> queue;
  std::unordered_set<std::pair<int, int>, pairHash> visited;

  std::pair<int, int> start = {0, 0};
  queue.push(start);
  visited.emplace(start);

  int level{};
  while (!queue.empty()) {
    int size = queue.size();

    while (size--) {
      auto node = queue.front();
      queue.pop();

      if (node.first == N - 1 && node.second == N - 1) {
        return level;
      }

      for (const auto& d : directions) {
        std::pair<int, int> next{node.first + d.first, node.second + d.second};
        if (next.first < 0 || next.first >= N || next.second < 0 ||
            next.second >= N || grid[next.first][next.second] == WALL ||
            visited.find(next) != visited.cend()) {
          continue;
        }

        queue.push(next);
        visited.emplace(next);
      }
    }

    level++;
  }

  return 0;
}

int main() {
  std::ifstream file("input.txt");
  if (!file.is_open()) {
    std::cerr << "Unable to open input.txt" << std::endl;
    return 1;
  }

  std::vector<std::string> fallingOrder;
  std::string line;

  while (std::getline(file, line)) {
    fallingOrder.emplace_back(line);
  }

  std::cout << "Part 1: " << part1(fallingOrder);
}
