#include <fstream>
#include <iostream>
#include <limits>
#include <queue>
#include <unordered_map>
#include <unordered_set>

const char WALL = '#';
const std::array<std::pair<int, int>, 4> directions{
    std::make_pair(-1, 0),
    std::make_pair(0, 1),
    std::make_pair(1, 0),
    std::make_pair(0, -1),
};

inline int clockwise(int d) { return (d + 1) % 4; }
inline int counterClosewise(int d) { return (d + 3) % 4; }

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

  bool operator==(const QueueNode& other) const {
    return d == other.d && node.first == other.node.first &&
           node.second == other.node.second;
  }
};

struct QueueNodeHash {
  inline std::size_t operator()(const QueueNode& qn) const {
    return qn.node.first ^ (qn.node.second << 1) ^ (qn.d << 2);
  }
};

using Path = std::unordered_set<QueueNode, QueueNodeHash>;

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

int countVisited(std::unordered_map<QueueNode, Path, QueueNodeHash>& path,
                 const std::pair<int, int>& start,
                 const std::pair<int, int>& end) {
  std::queue<QueueNode> queue;
  std::unordered_set<QueueNode, QueueNodeHash> visited;
  std::unordered_set<std::pair<int, int>, pairHash> nodes;

  for (int i = 0; i < 4; i++) {
    auto node = QueueNode{.node = end, .d = i};
    queue.push(node);
    visited.insert(node);
  }

  while (!queue.empty()) {
    auto node = queue.front();
    queue.pop();
    nodes.insert(node.node);

    for (const auto& next : path[node]) {
      if (visited.find(next) == visited.cend()) {
        queue.push(next);
        visited.insert(next);
      }
    }
  }

  return nodes.size();
}

std::pair<int, int> dijkstra(const std::vector<std::string>& grid) {
  const int N = grid.size(), M = grid[0].size();
  int score = std::numeric_limits<int>::max();
  auto [start, end] = findStartEnd(grid);

  std::priority_queue<QueueNode> queue;
  std::unordered_map<QueueNode, Path, QueueNodeHash> visited;
  std::unordered_map<QueueNode, int, QueueNodeHash> costs;
  auto qn = QueueNode{.score = 0, .node = start, .d = 1};
  queue.push(qn);
  visited[qn].emplace(qn);
  costs[qn] = 0;

  auto process = [&](QueueNode& node, std::pair<int, int>& next, int d,
                     int cost) {
    if (!bounded(next, N, M) || grid[next.first][next.second] == WALL) {
      return;
    }

    QueueNode nextNode = {.node = next, .score = node.score + cost, .d = d};
    if (visited.find(nextNode) != visited.cend()) {
      if (nextNode.score == costs[nextNode]) {
        visited[nextNode].insert(node);  // Equally good path.
      } else if (nextNode.score < costs[nextNode]) {
        // Found better path.
        visited[nextNode].clear();
        visited[nextNode].insert(node);
        costs[nextNode] = nextNode.score;
      }

      return;
    }

    // Add to queue.
    queue.emplace(nextNode);
    visited[nextNode].insert(node);
    costs[nextNode] = nextNode.score;
  };

  while (!queue.empty()) {
    auto node = queue.top();
    queue.pop();

    if (node.node.first == end.first && node.node.second == end.second) {
      // Reached the end. Record if this is the shortest path.
      if (node.score > score) {
        break;  // No more optimal paths.
      }

      score = node.score;
    }

    std::pair<int, int> advance = {
        node.node.first + directions[node.d].first,
        node.node.second + directions[node.d].second};

    process(node, advance, node.d, 1);
    process(node, node.node, clockwise(node.d), 1000);
    process(node, node.node, counterClosewise(node.d), 1000);
  }

  return {score, countVisited(visited, start, end)};
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
