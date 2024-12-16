#include <format>
#include <fstream>
#include <iostream>
#include <limits>
#include <queue>
#include <unordered_map>
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

struct pairEqual {
  bool operator()(const std::pair<int, int>& lhs,
                  const std::pair<int, int>& rhs) const {
    return lhs.first == rhs.first && lhs.second == rhs.second;
  }
};

using Path = std::unordered_set<std::pair<int, int>, pairHash>;

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

int countVisited(const std::vector<std::string>& grid,
                 const std::unordered_map<std::pair<int, int>, Path, pairHash,
                                          pairEqual>& visited,
                 const std::pair<int, int>& start,
                 const std::pair<int, int>& cur, Path& counted) {
  std::cout << std::format("-- ({}, {})\n", cur.first, cur.second);
  if (cur == start) {
    return 0;
  }

  int count{};
  for (const std::pair<int, int>& node : visited.at(cur)) {
    if (counted.find(node) == counted.cend()) {
      counted.insert(node);
      count += 1 + countVisited(grid, visited, start, node, counted);
    }
  }

  return count;
}

std::pair<int, int> dijkstra(const std::vector<std::string>& grid) {
  const int N = grid.size(), M = grid[0].size();
  std::pair<int, int> result{std::numeric_limits<int>::max(), 0};
  auto [start, end] = findStartEnd(grid);

  std::priority_queue<QueueNode> queue;
  std::unordered_map<std::pair<int, int>, Path, pairHash, pairEqual> visited;
  std::unordered_map<std::pair<int, int>, int, pairHash, pairEqual> costs;
  queue.emplace(QueueNode{.score = 0, .node = start, .d = 1});
  visited[start].emplace(start);
  costs[start] = 0;

  auto process = [&](QueueNode& node, int d, int cost) {
    std::pair<int, int> next{node.node.first + directions[d].first,
                             node.node.second + directions[d].second};
    if (!bounded(next, N, M) || grid[next.first][next.second] == WALL) {
      return;
    }

    std::cout << std::format("({}, {}) -> ({}, {})\n", node.node.first, node.node.second, next.first, next.second);

    int nextCost = node.score + cost;
    if (auto it = visited.find(next); it != visited.cend()) {
      if (nextCost == costs[next]) {
        visited[next].insert(node.node);
      } else if (nextCost < costs[next]) {
        visited[next].clear();
        visited[next].insert(node.node);
        costs[next] = nextCost;
      }

      return;
    }

    
    queue.emplace(QueueNode{.score = nextCost, .node = next, .d = d});
    visited[next].insert(node.node);
    costs[next] = nextCost;
  };

  while (!queue.empty()) {
    auto node = queue.top();
    queue.pop();

    if (node.node.first == end.first && node.node.second == end.second) {
      // Reached the end. Record if this is the shortest path.
      if (node.score > result.first) {
        break;  // No more optimal paths.
      }

      result.first = node.score;
    }

    process(node, node.d, 1);
    process(node, clockwise(node.d), 1000);
    process(node, counterClosewise(node.d), 1000);
  }

  std::cout << "=====" << std::endl;
  for (auto& kv : visited) {
    std::cout << std::format("({}, {}) -> ", kv.first.first, kv.first.second);
    for (auto& n : kv.second) {
      std::cout << std::format("({}, {}) ", n.first, n.second);
    }
    std::cout << std::endl;
  }

  Path counted;
  counted.insert(end);
  result.second = countVisited(grid, visited, start, end, counted) + 1;
  return result;
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

  auto result = dijkstra(grid);
  std::cout << "Part 1: " << result.first << std::endl;
  std::cout << "Part 2: " << result.second << std::endl;
}
