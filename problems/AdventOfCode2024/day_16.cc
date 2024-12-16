#include <fstream>
#include <iostream>
#include <queue>
#include <unordered_set>

const char EMPTY = '.';
const char WALL = '#';
const std::array<std::pair<int, int>, 4> directions{
    std::make_pair(-1, 0),
    std::make_pair(0, 1),
    std::make_pair(1, 0),
    std::make_pair(0, -1),
};

inline int clockwise(int d) { return (d + 1) % 4; }

inline int counterClosewise(int d) {
  if (d == 0) {
    return 3;
  }

  return d - 1;
}

struct pairHash {
  inline std::size_t operator()(const std::pair<int, int>& p) const {
    return p.first ^ (p.second << 1);
  }
};

struct QueueNode {
  std::pair<int, int> node;
  int d, score;

  bool operator<(const QueueNode& other) const {
    return score > other.score;  // Force min-heap.
  }
};

inline bool bounded(const std::pair<int, int>& cell, const int N, const int M) {
  return cell.first >= 0 && cell.first < N && cell.second >= 0 &&
         cell.second < M;
}

std::pair<std::pair<int, int>, std::pair<int, int>> findStartEnd(
    const std::vector<std::string>& grid) {
  const int N = grid.size(), M = grid[0].size();
  std::pair<int, int> start, end;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (grid[i][j] == 'S') {
        start.first = i;
        start.second = j;
      } else if (grid[i][j] == 'E') {
        end.first = i;
        end.second = j;
      }
    }
  }

  return {start, end};
}

int part1(const std::vector<std::string>& grid) {
  const int N = grid.size(), M = grid[0].size();
  auto [start, end] = findStartEnd(grid);

  std::priority_queue<QueueNode> queue;
  std::unordered_set<std::pair<int, int>, pairHash> visited;
  queue.emplace(QueueNode{.score = 0, .node = start, .d = 1});
  visited.insert(start);

  auto process = [&](QueueNode& node, int d, int cost) {
    std::pair<int, int> next{node.node.first + directions[d].first,
                             node.node.second + directions[d].second};
    if (!bounded(next, N, M) || grid[next.first][next.second] == WALL ||
        visited.find(next) != visited.cend()) {
      return;
    }

    queue.emplace(QueueNode{.score = node.score + cost, .node = next, .d = d});
    visited.emplace(next);
  };

  while (!queue.empty()) {
    auto node = queue.top();
    queue.pop();

    if (node.node.first == end.first && node.node.second == end.second) {
      return node.score;  // Found the shortest path!
    }

    process(node, node.d, 1);
    process(node, clockwise(node.d), 1001);
    process(node, counterClosewise(node.d), 1001);
  }

  return -1;
}

int main() {
  std::ifstream file("input.txt");
  if (!file.is_open()) {
    std::cerr << "Unable to open input.txt" << std::endl;
    return 1;
  }

  std::vector<std::string> grid;
  std::string line;

  while (std::getline(file, line)) {
    grid.emplace_back(line);
  }

  std::cout << "Part 1: " << part1(grid) << std::endl;
}
