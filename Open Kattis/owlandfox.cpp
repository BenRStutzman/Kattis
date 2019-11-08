#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N;
	cin >> N;
	int n;
	vector <int> v;	
	while (N--) {
		v.clear();
		cin >> n;
		while (n) {
			v.push_back(n % 10);
			n /= 10;
		}
		for (int i = 0; i < v.size(); ++i) {
			//cout << "v[i]: " << v[i] << endl;
			if (v[i]) {
				v[i]--;
				break;
			}
		}
		reverse(v.begin(), v.end());
		for (int i : v) {
			//cout << "i: " << i << endl;
			n = n * 10 + i;
		}
		cout << n << endl;
	}

	return 0;
}
