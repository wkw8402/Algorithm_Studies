#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
int population[25][25] = {0};
bool visited[25][25];

int checkRows[] = {0, 1, 0, -1};
int checkColumns[] = {-1, 0, 1, 0};

int findGroup(int x, int y) {
    visited[x][y] = true;
    int count = 0;
    for (int i = 0; i < 4; i++) {
        int closeRows = x + checkRows[i];
        int closeColumns = y + checkColumns[i];

        bool withinRange = closeRows >= 0 && closeColumns >= 0 && closeRows < N && closeColumns < N;

        if (withinRange && population[closeRows][closeColumns] == 1 && !visited[closeRows][closeColumns]) {
            visited[closeRows][closeColumns] = true;
            count++;
            count += findGroup(closeRows, closeColumns);
        }
    }
    return count;
}
int main(void) {
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (scanf("%1d", &population[i][j]) == 1) {
                ;
            }
        }
    }
    vector<int> group;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (population[i][j] == 1 && !visited[i][j]) group.push_back(1 + findGroup(i, j));
        }
    }

    sort(group.begin(), group.end(), greater<>());

    cout << group.size() << endl;
    for (int member : group) {
        cout << member << " ";
    }
    return 0;
}