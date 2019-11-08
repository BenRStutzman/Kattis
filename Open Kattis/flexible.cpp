#include <iostream>
#include <set>
#include <vector>

using namespace std;

int main() {
	set <int> partitions;
	int W, M;
	cin >> W >> M;
	vector <int> walls (M + 2, 0);
	int i = 1;
	int x;

	for (int j = 0; j < M; ++j) {
		cin >> x;
		walls[i] = x;
		for (int j = 0; j < i; ++j)	partitions.insert(x - walls[j]);
		++i;
	}

	for (int j = 0; j < M + 1; ++j) {
		rout << j << endl;
		cout << W - walls[j] << endl;
		partitions.insert(W - walls[j]);
	}
	
	for (set <int>::iterator it = partitions.begin(); it != partitions.end();
			++it) {
		cout << *it << endl;
	}
	return 0;
}
