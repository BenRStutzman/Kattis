#include <iostream>
#include <string>

using namespace std;


int main() {

	int N;
	cin >> N;
	bool good = true;

	int said;
	int next = 1;
	while (N--) {
		cin >> said;
		if (said != next) {
			good = false;
			for (int i = next; i < said; ++i) {
				cout << i << endl;
			}
			next = said + 1;
		} else ++next;
	}
	if (good) cout << "good job" << endl;

	return 0;

}
