#include <iostream>


using namespace std;


int main() {
	int bin;
	int max_bin;
	int N;
	cin >> N;
	int k, n;
	while (N--) {
		cin >> k >> n;
		int bins[81] = {};
		bins[0] = n;
		bin = 0;
		max_bin = 0;
		while (n--) {
			while (bins[bin]) {
				bins[bin] -= 1;
				++bin;
			}	
			//cout << "bin: " << bin << endl;
			if (bin > max_bin) max_bin = bin;
			bins[bin] = bin;
			bin = 0;
		}
		cout << k << " " << max_bin;
		for (int i = 1; i <= max_bin; ++i) {
			if (i % 10 == 1) cout << endl; 
			cout << bins[i] << " ";
		}
		cout << endl;
	}
	
	return 0;

}
