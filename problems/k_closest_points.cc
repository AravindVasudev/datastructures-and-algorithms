#include <vector>
#include <cmath>
#include <cstdio>
#include <map>

int main() {
    std::vector<std::pair<int, int>> points = {std::pair<int, int>(-2, 4),
                                               std::pair<int, int>(0, -2),
                                               std::pair<int, int>(-1, 0),
                                               std::pair<int, int>(3, 5),
                                               std::pair<int, int>(-2, -3),
                                               std::pair<int, int>(3, 2)};

    int k = 3;

    std::map<double, std::pair<int, int>> distance_map;
    for (const auto& point : points) {
        const double distance = std::sqrt(std::pow(point.first, 2) + std::pow(point.second, 2));
        distance_map[distance] = point;
    }

    for (const std::pair<double, std::pair<int, int>>& dpoint : distance_map) {
        if (!k--) break;
        printf("(%d, %d)\n", dpoint.second.first, dpoint.second.second);
    }

    return 0;
}
