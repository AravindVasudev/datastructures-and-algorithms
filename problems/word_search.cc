#include <iostream>
#include <string>

using namespace std;

#define R 5
#define C 5

int dir[8][2] = { {-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1} };

bool search2D(string grid[], string word, int row, int col) {
    if (grid[row][col] != word[0])
        return false;

    int len = word.length();
    for (int d = 0; d < 8; d++) {
        int k = 0, rd = row + dir[d][0], cd = col + dir[d][1];

        for (k = 1; k < len; k++) {
            if (rd >= R || rd < 0 || cd >= C || cd < 0)
                break;

            if (word[k] != grid[rd][cd])
                break;

            rd += dir[d][0];
            cd += dir[d][1];
        }

        if (k == len) return true;
    }

    return false;
}

void search(string grid[], string word) {
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            if (search2D(grid, word, i, j))
                cout << word << " found at: " << i << ", " << j << endl;
}

int main() {
    string grid[R] = { "MOREM", "UPSUM", "SMURT", "OMMDL", "BMUSA" };

    search(grid, "SUM");

    return 0;
}
