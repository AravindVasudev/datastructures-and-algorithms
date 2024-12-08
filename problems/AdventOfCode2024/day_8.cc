/*
$ hyperfine --runs 10 ./day_8
Benchmark 1: ./day_8
  Time (mean ± σ):       1.6 ms ±   0.3 ms    [User: 1.0 ms, System: 0.3 ms]
  Range (min … max):     1.3 ms …   2.4 ms    10 runs

  Warning: Command took less than 5 ms to complete. Note that the results might be inaccurate because hyperfine can not calibrate the shell startup time much more precise than this limit. You can try to use the `-N`/`--shell=none` option to disable the shell completely.
*/
#include <fstream>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <unordered_set>

struct pairHash {
  inline std::size_t operator()(const std::pair<int, int>& p) const {
    return p.first * 1000 + p.second;
  }
};

std::pair<int, int> antinode(std::pair<int, int> p1, std::pair<int, int> m) {
  // midpoint: (xm, ym) = [(x1 + x2) / 2, (y1 + y2) / 2]
  // (x2, y2) = [(2xm - x1), (2ym - y1)]
  return {(2 * m.first - p1.first), (2 * m.second - p1.second)};
}

std::unordered_map<char, std::vector<std::pair<int, int>>> findAntennas(
    const std::vector<std::string>& grid) {
  std::unordered_map<char, std::vector<std::pair<int, int>>> antennas;
  const int N = grid.size(), M = grid[0].size();
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (grid[i][j] != '.') {
        antennas[grid[i][j]].push_back({i, j});
      }
    }
  }

  // Remove all the solo-antennas.
  for (auto it = antennas.begin(); it != antennas.end();) {
    if (it->second.size() < 2) {
      it = antennas.erase(it);
    } else {
      it++;
    }
  }

  return antennas;
}

int part1(const std::vector<std::string>& grid,
          const std::unordered_map<char, std::vector<std::pair<int, int>>>&
              antennas) {
  const int N = grid.size(), M = grid[0].size();

  std::unordered_set<std::pair<int, int>, pairHash> points;
  auto isBounded = [&N, &M](const std::pair<int, int>& point) {
    return point.first >= 0 && point.first < N && point.second >= 0 &&
           point.second < M;
  };

  for (const auto& kv : antennas) {
    const int S = kv.second.size();
    for (int i = 0; i < S; i++) {
      for (int j = i + 1; j < S; j++) {
        auto antiNode1 = antinode(kv.second[i], kv.second[j]);
        auto antiNode2 = antinode(kv.second[j], kv.second[i]);

        if (isBounded(antiNode1)) {
          points.emplace(antiNode1);
        }

        if (isBounded(antiNode2)) {
          points.emplace(antiNode2);
        }
      }
    }
  }

  return points.size();
}

double slope(double x1, double y1, double x2, double y2) {
  if (x1 == x2) {
    return std::numeric_limits<double>::infinity();
  }

  return (y2 - y1) / (x2 - x1);
}

// Check if the given point is an antinode.
bool check(
    const std::unordered_map<char, std::vector<std::pair<int, int>>>& antennas,
    int x, int y) {
  for (const auto& kv : antennas) {
    const int N = kv.second.size();
    for (int i = 0; i < N; i++) {
      if (kv.second[i].first == x && kv.second[i].second == y) {
        return true;  // Antenna itself is an antinode.
      }

      auto m1 = slope(x, y, kv.second[i].first, kv.second[i].second);
      for (int j = i + 1; j < N; j++) {
        auto m2 = slope(kv.second[i].first, kv.second[i].second,
                        kv.second[j].first, kv.second[j].second);

        if (m1 == m2) {
          return true;
        }
      }
    }
  }

  return false;
}

int part2(const std::vector<std::string>& grid,
          const std::unordered_map<char, std::vector<std::pair<int, int>>>&
              antennas) {
  const int N = grid.size(), M = grid[0].size();
  int count{};

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (check(antennas, i, j)) {
        count++;
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

  std::vector<std::string> grid;
  std::string line;

  while (getline(input, line)) {
    grid.emplace_back(line);
  }

  input.close();

  auto antennas = findAntennas(grid);
  std::cout << "Part 1: " << part1(grid, antennas) << std::endl;
  std::cout << "Part 2: " << part2(grid, antennas) << std::endl;
}
