#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <sstream>

int computeDistance(std::vector<int>& list1, std::vector<int>& list2) {
    // Sort the lists.
    std::sort(list1.begin(), list1.end());
    std::sort(list2.begin(), list2.end());

    const int N = list1.size();
    int distance{0};

    for (int i = 0; i < N; i++) {
        distance += abs(list1[i] - list2[i]);
    }

    return distance;
}

int computeSimilarityScore(const std::vector<int>& list1, const std::vector<int>& list2) {
    std::unordered_map<int, int> rightOccurence;
    for (const int num : list2) {
        rightOccurence[num]++;
    }

    int similarityScore{};
    for (const int num : list1) {
        similarityScore += rightOccurence[num] * num;
    }

    return similarityScore;
}

int main() {
    std::ifstream input("input.txt");
    if (!input.is_open()) {
        std::cerr << "Error: Unable to open file." << std::endl;
        return 1;
    }

    std::string line;
    std::vector<int> list1, list2;
    while (std::getline(input, line)) {
        std::istringstream lineStream(line);
        int num1, num2;

        lineStream >> num1 >> num2;
        list1.push_back(num1);
        list2.push_back(num2);
    }

    input.close();

    std::cout << "Distance: " << computeDistance(list1, list2) << std::endl;
    std::cout << "Similarity Score: " << computeSimilarityScore(list1, list2) << std::endl;
}