#include <iostream>
#include <vector>

using namespace std;

int main() {
	int N, M;

	cin >> N >> M;
	if (M >= N) {
		cout << "too late" << endl;
		return 0;
	}
	
	vector <bool> taken (N + 1, false);
	int n;
	while (M--) {
		cin >> n;
		taken[n] = true;
	}
	for (int i = 1; i <= N; ++i) {
		//cout << "it: " << *it << ", i: " << i << endl;
		if (!taken[i]) {
			cout << i << endl;
			return 0;
		}
	}
	return 0;
}
