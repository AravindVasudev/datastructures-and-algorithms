#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <unordered_set>
#include <vector>

// Splits "X|Y" -> {X, Y}.
std::pair<int, int> splitEdge(const std::string& edge) {
  const size_t delimiter = edge.find('|');
  return {std::stoi(edge.substr(0, delimiter)),
          std::stoi(edge.substr(delimiter + 1))};
}

// converts "x,y,z" -> {x, y, z}.
std::vector<int> splitPages(const std::string& pages) {
  std::stringstream stream(pages);
  std::vector<int> manual;

  std::string page;
  while (std::getline(stream, page, ',')) {
    manual.push_back(std::stoi(page));
  }

  return manual;
}

// Returns topological sort of the graph using Kahn's Algorithm.
std::vector<int> topologicalSort(
    const std::unordered_map<int, std::vector<int>>& graph) {
  std::vector<int> sorted;
  std::unordered_map<int, int> inDegree;

  // Compute inDegree for all nodes.
  for (const auto& kv : graph) {
    for (int outNode : kv.second) {
      inDegree[outNode]++;
    }
  }

  // Add all nodes with no in-degree.
  std::queue<int> queue;
  for (const auto& kv : graph) {
    if (inDegree[kv.first] == 0) {
      queue.push(kv.first);
    }
  }

  while (!queue.empty()) {
    int cur = queue.front();
    queue.pop();
    sorted.push_back(cur);

    // Decrease in-degree for all neighbors.
    if (graph.find(cur) == graph.end()) {
      continue;
    }

    const auto& neighbors = graph.at(cur);
    for (int neighbor : neighbors) {
      inDegree[neighbor]--;
      if (inDegree[neighbor] == 0) {
        queue.push(neighbor);
      }
    }
  }

  // Skip cycle check.
  return sorted;
}

std::unordered_map<int, std::vector<int>> generateSubgraph(
    const std::vector<std::pair<int, int>>& edges,
    const std::vector<int>& manual) {
  std::unordered_set<int> uniquePages(manual.cbegin(), manual.cend());
  std::unordered_map<int, std::vector<int>> graph;

  for (const auto& edge : edges) {
    // Only add edge if it's revelant to the given manual.
    if (uniquePages.find(edge.first) != uniquePages.end() && uniquePages.find(edge.second) != uniquePages.end()) {
      graph[edge.first].push_back(edge.second);
    }
  }

  return graph;
}

int validManualSum(const std::vector<std::vector<int>>& manuals,
                   const std::vector<std::pair<int, int>>& edges) {
  int sum{};
  for (auto manual : manuals) {
    const auto ordering = topologicalSort(generateSubgraph(edges, manual));
    if (manual == ordering) {
      sum += manual[manual.size() / 2];
    }
  }

  return sum;
}

int invalidManualSum(const std::vector<std::vector<int>>& manuals,
                     const std::vector<std::pair<int, int>>& edges) {
  int sum{};
  for (auto manual : manuals) {
    const auto ordering = topologicalSort(generateSubgraph(edges, manual));
    if (manual != ordering) {
      sum += ordering[ordering.size() / 2];
    }
  }

  return sum;
}

int main() {
  std::ifstream input("input.txt");
  if (!input.is_open()) {
    std::cerr << "Error: Unable to open input.txt" << std::endl;
    return 1;
  }

  std::vector<std::pair<int, int>> edges;
  std::vector<std::vector<int>> manuals;
  std::string line;

  // Parse all the edges.
  while (getline(input, line)) {
    if (line.empty()) {
      break;
    }

    edges.emplace_back(splitEdge(line));
  }

  // Read all the pages.
  while (getline(input, line)) {
    manuals.emplace_back(splitPages(line));
  }

  std::cout << "∑(middle valid pages): " << validManualSum(manuals, edges)
            << std::endl;
  std::cout << "∑(middle invalid pages): " << invalidManualSum(manuals, edges)
            << std::endl;
}
