#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

struct Point {
  long X, Y, Z;

  bool operator==(Point const& other) const {
    return X == other.X && Y == other.Y && Z == other.Z;
  }

  long distance(Point p) {
    return sqrt(pow(p.X - X, 2) + pow(p.Y - Y, 2) + pow(p.Z - Z, 2));
  }
};

struct PointHash {
  size_t operator()(Point const& p) const noexcept {
    return p.X ^ (p.Y << 1) ^ (p.Z << 2);
  }
};

inline std::ostream& operator<<(std::ostream& os, const Point& p) {
  os << "(" << p.X << ", " << p.Y << ", " << p.Z << ")";
  return os;
}

struct UnionFind {
  std::unordered_map<Point, Point, PointHash> parent;
  std::unordered_map<Point, int, PointHash> sizes;
  int groups{};

  UnionFind(const std::vector<Point>& points) {
    for (const auto& point : points) {
      parent[point] = point;
      sizes[point] = 1;
      groups++;
    }
  }

  Point find(const Point& point) {
    if (parent[point] == point) {
      return point;
    }

    parent[point] = find(parent[point]);  // Path compression
    return parent[point];
  }

  bool unionSets(Point p1, Point p2) {
    p1 = find(p1);
    p2 = find(p2);

    if (p1 == p2) {
      return false;  // Already in the same set.
    }

    // union by size
    if (sizes[p1] < sizes[p2]) {
      std::swap(p1, p2);
    }

    parent[p2] = p1;
    sizes[p1] += sizes[p2];
    groups--;
    return true;
  }

  bool isRoot(const Point& p) { return parent[p] == p; }

  std::vector<int> findRootSizes() {
    std::vector<int> rootSizes;
    for (const auto& [k, v] : sizes) {
      if (isRoot(k)) {
        rootSizes.push_back(v);
      }
    }

    std::sort(rootSizes.begin(), rootSizes.end(), std::greater<int>());
    return rootSizes;
  }
};

std::vector<std::pair<Point, Point>> generateSortedPairs(
    const std::vector<Point>& junctions) {
  // Generate pairs.
  const auto size = junctions.size();
  std::vector<std::pair<Point, Point>> pairs;
  for (int i = 0; i < size; i++) {
    for (int j = i + 1; j < size; j++) {
      pairs.push_back({junctions[i], junctions[j]});
    }
  }

  // Sort them by distance.
  std::sort(pairs.begin(), pairs.end(),
            [](std::pair<Point, Point> a, std::pair<Point, Point> b) {
              return a.first.distance(a.second) < b.first.distance(b.second);
            });

  return pairs;
}

std::pair<long, long> connect(const std::vector<Point>& junctions, int N = 1000) {
  const auto pairs = generateSortedPairs(junctions);
  auto uf = UnionFind(junctions);

  // Union the first N shortest pairs.
  for (int i = 0; i < N; i++) {
    uf.unionSets(pairs[i].first, pairs[i].second);
  }

  // Part-1: product of top three group sizes.
  const auto sizes = uf.findRootSizes();
  long p1 = sizes[0] * sizes[1] * sizes[2];

  // Part-2: Continue unioning until everything is connected.
  long p2{};
  for (int i = N; i < pairs.size(); i++) {
    uf.unionSets(pairs[i].first, pairs[i].second);

    // All groups are combined.
    if (uf.groups == 1) {
      p2 = pairs[i].first.X * pairs[i].second.X;
      break;
    }
  }

  return {p1, p2};
}

int main() {
  // Read input file.
  std::ifstream input("input.txt");
  if (!input.is_open()) {
    std::cerr << "Error: Unable to open input.txt" << std::endl;
    return 1;
  }

  std::vector<Point> junctions;
  std::string line;
  while (std::getline(input, line)) {
    std::istringstream iss(line);
    std::string token;
    Point p;

    std::getline(iss, token, ',');
    p.X = std::stol(token);

    std::getline(iss, token, ',');
    p.Y = std::stol(token);

    std::getline(iss, token);
    p.Z = std::stol(token);

    junctions.push_back(p);
  }

  const auto [p1, p2] = connect(junctions);
  std::cout << "Part 1: " << p1 << std::endl;
  std::cout << "Part 2: " << p2 << std::endl;
}