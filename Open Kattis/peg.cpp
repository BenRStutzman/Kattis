#include <iostream>
#include <string>

using namespace std;

int main() {
	string board[9];
	board[0] = board[8] = "         ";
	string row;
	int count = 0;
	for (int i = 0; i < 7; ++i) {
		getline(cin, row);
		board[i + 1] = " " + row + " ";
	}
	int tries[4][4] = {{-1, 0, 1, 0}, {1, 0, -1, 0}, {0, 1, 0, -1}, {0, -1, 0, 1}};
	for (int i = 1; i < 8; ++i) {
		for (int j = 1; j < 8; ++j) {
			if (board[i][j] == 'o') {
				for (auto dir : tries) {
					if (board[i + dir[0]][j + dir[1]] == '.' &&
						board[i + dir[2]][j + dir[3]] == 'o') {
						++count;
					}
				}
			}
		}
	}
				
	cout << count << endl;

	return 0;
}
