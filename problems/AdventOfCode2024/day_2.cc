#include <cmath>
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

bool isReportSafe(const std::vector<int>& report) {
    int N = report.size();
    bool increasing = report[0] < report[1];
    for (int i = 1; i < N; i++) {
        if (increasing) {
            if (report[i - 1] >= report[i] || report[i] - report[i - 1] > 3) {
                return false;
            }
        } else {
            if (report[i - 1] <= report[i] || report[i - 1] - report[i] > 3) {
                return false;
            }
        }
    }

    return true;
}

int countSafeReports(const std::vector< std::vector<int> >& reports) {
    int count{};
    for (const std::vector<int>& report : reports) {
        if (isReportSafe(report)) {
            count++;
        }
    }

    return count;
}

int countSafeReportsWithDampening(std::vector< std::vector<int> >& reports) {
    int count{};
    for (std::vector<int>& report : reports) {
        if (isReportSafe(report)) {
            count++;
            continue;
        }

        const int N = report.size();
        for (int i = 0; i < N; i++) {
            int level = report[i];
            report.erase(report.begin() + i);
            if (isReportSafe(report)) {
                count++;
                break;
            }

            report.insert(report.begin() + i, level);
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

    std::string line;
    std::vector< std::vector<int> > reports;
    while (std::getline(input, line)) {
        std::istringstream lineStream(line);
        std::vector<int> report;
        int num;

        while (lineStream >> num) {
            report.push_back(num);
        }

        reports.push_back(report);
    }

    input.close();

    std::cout << "Safe Reports: " << countSafeReports(reports) << std::endl;
    std::cout << "Safe Reports (w/ Dampening): " << countSafeReportsWithDampening(reports) << std::endl;
}
