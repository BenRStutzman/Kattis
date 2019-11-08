#include <iostream>
#include <climits>

using namespace std;

int main() {
	int case_num = 0;
	int n;
	int cur_num;

	while (cin >> n) {
		case_num++;
		int min = INT_MAX;
		int max = INT_MIN;
		while (n--) {
			cin >> cur_num;
			if (cur_num < min) min = cur_num;
			if (cur_num > max) max = cur_num;
		}
		cout << "Case " << case_num << ": " << min << " "
		<< max << " " << max - min << endl;
	}
	return 0;
}
