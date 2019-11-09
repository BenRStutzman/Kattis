#include <iostream>

using namespace std;

int main() {

	int limit = 100;
	int i, j;
	long e[limit + 1][limit + 1];
	for (i = 0; i <= limit; i++) e[i][0] = 1;
	for (j = 0; j <= limit; j++) e[0][j] = 0;
	for (i = 1; i <= limit; i++) {
		for (j = 1; j < i; j++) {
			e[i][j] = ((j + 1) * e[i - 1][j] + (i - j) * e[i - 1][j - 1]) % 1001113;
		}
	}


	int N;
	cin >> N;
	int a, n, k;
	while (N--) {
		cin >> a >> n >> k;
		//cout << n << " " << k << endl;
		cout << a << " " << e[n][k] << endl;
	}
	return 0;
}
