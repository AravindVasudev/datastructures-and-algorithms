#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <vector>
#include <unordered_set>

// Inserts "X|Y" edge into the given graph.
void addEdge(std::unordered_map<int, std::vector<int>>& graph,
             const std::string& edge) {
  const size_t delimiter = edge.find('|');
  const int inNode = std::stoi(edge.substr(0, delimiter));
  const int outNode = std::stoi(edge.substr(delimiter + 1));

  graph[inNode].push_back(outNode);
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

std::unordered_map<int, std::vector<int>> generateSubset(
    const std::unordered_map<int, std::vector<int>>& graph,
    const std::vector<int>& manual) {
  std::unordered_set<int> uniquePages(manual.cbegin(), manual.cend());
  std::unordered_map<int, std::vector<int>> subset(graph); // clone.

  for (auto it = subset.begin(); it != subset.end();) {
    if (uniquePages.find(it->first) == uniquePages.end()) {
      it = subset.erase(it); // Remove entire node.
      continue;
    }

    // Remove unfound neighbors.
    auto& neighbors = it->second;
    for (auto el = neighbors.begin(); el != neighbors.end();) {
      if (uniquePages.find(*el) == uniquePages.end()) {
        el = neighbors.erase(el);
      } else {
        el++;
      }
    }

    it++;
  }

  return subset;
}

int validManualSum(const std::vector<std::vector<int>>& manuals,
                   const std::unordered_map<int, std::vector<int>>& graph) {
  int sum{};
  for (auto manual : manuals) {
    const auto ordering = topologicalSort(generateSubset(graph, manual));
    if (manual == ordering) {
      sum += manual[manual.size() / 2];
    }
  }

  return sum;
}

int invalidManualSum(const std::vector<std::vector<int>>& manuals,
                     const std::unordered_map<int, std::vector<int>>& graph) {
  int sum{};
  for (auto manual : manuals) {
    const auto ordering = topologicalSort(generateSubset(graph, manual));

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

  std::unordered_map<int, std::vector<int>> graph;
  std::string line;

  // Parse all the edges.
  while (getline(input, line)) {
    if (line.empty()) {
      break;
    }

    addEdge(graph, line);
  }

  // Read all the pages.
  std::vector<std::vector<int>> manuals;
  while (getline(input, line)) {
    manuals.emplace_back(splitPages(line));
  }

  std::cout << "∑(middle valid pages): " << validManualSum(manuals, graph)
            << std::endl;
  std::cout << "∑(middle invalid pages): " << invalidManualSum(manuals, graph)
            << std::endl;
}
