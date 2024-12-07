/******
* Instructions for Apple Silicon (M1 Pro):

```
$ brew install folly
$ g++ -std=c++20 -I /opt/homebrew/Cellar/folly/2024.12.02.00/include -I
/opt/homebrew/Cellar/boost/1.86.0/include -I
/opt/homebrew/Cellar/glog/0.6.0/include -I
/opt/homebrew/Cellar/gflags/2.2.2/include -I
/opt/homebrew/Cellar/double-conversion/3.3.0/include -I
/opt/homebrew/Cellar/fmt/11.0.2/include -I
/opt/homebrew/Cellar/libevent/2.1.12_1/include -L
/opt/homebrew/Cellar/folly/2024.12.02.00/lib -L
/opt/homebrew/Cellar/boost/1.86.0/lib -L /opt/homebrew/Cellar/glog/0.6.0/lib -L
/opt/homebrew/Cellar/gflags/2.2.2/lib -L
/opt/homebrew/Cellar/double-conversion/3.3.0/lib -L
/opt/homebrew/Cellar/fmt/11.0.2/lib -L
/opt/homebrew/Cellar/libevent/2.1.12_1/lib -lfolly -lglog -O3 day_6.cc -o day_6
$ ./day_6
# of distinct positions: 5551
# of possibilites: 1939

$ hyperfine --runs 10 ./day_6
Benchmark 1: ./day_6
  Time (mean ± σ):      21.5 ms ±   0.8 ms    [User: 84.6 ms, System: 4.5 ms]
  Range (min … max):    20.3 ms …  22.9 ms    10 runs

# Just Part-2
$ hyperfine --runs 10 ./day_6
Benchmark 1: ./day_6
  Time (mean ± σ):      21.3 ms ±   0.7 ms    [User: 84.0 ms, System: 4.6 ms]
  Range (min … max):    20.4 ms …  22.7 ms    10 runs
```

******/

#include <folly/executors/CPUThreadPoolExecutor.h>
#include <folly/futures/Future.h>

#include <fstream>
#include <iostream>
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

inline int hashState(const int X, const int Y, const std::pair<int, int>& d) {
  return (X * 130 + Y) * 130 + (d.first * 10 + d.second);
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
              std::pair<int, int> position,
              const std::pair<int, int>& newObstacle) {
  const int N = grid.size(), M = grid[0].size();
  int d = 0;
  std::unordered_set<int> states;
  states.insert(hashState(position.first, position.second, directions[d]));

  // Brute force walk through the grid.
  while (true) {
    int nextX = position.first + directions[d].first;
    int nextY = position.second + directions[d].second;

    if (nextX < 0 || nextX >= N || nextY < 0 || nextY >= M) {
      break;  // left the grid.
    }

    if (grid[nextX][nextY] == '#' ||
        (newObstacle.first == nextX && newObstacle.second == nextY)) {
      d = (d + 1) % directions.size();  // turn right.

      const int state = hashState(nextX, nextY, directions[d]);
      if (states.find(state) != states.end()) {
        return true;  // loop
      }
      states.emplace(state);

      continue;
    }

    position.first = nextX;
    position.second = nextY;
  }

  return false;
}

int part1(std::vector<std::string>& grid, const std::pair<int, int>& position) {
  return getDistinctPath(grid, position).size();
}

int part2(std::vector<std::string>& grid, const std::pair<int, int>& position) {
  int count{};
  auto options = getDistinctPath(grid, position);

  const auto numCores = std::thread::hardware_concurrency();
  folly::CPUThreadPoolExecutor executor(numCores);
  std::vector<folly::Future<bool>> futures;

  for (const auto& option : options) {
    if (option.first == position.first && option.second == position.second) {
      continue;  // skip start.
    }

    futures.push_back(folly::via(
        &executor, [&]() { return doesLoop(grid, position, option); }));
  }

  auto results = folly::collectAll(futures).get();  // wait.
  for (const auto& f : results) {
    if (f.value()) {
      count++;
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
