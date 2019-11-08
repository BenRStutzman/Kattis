#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int N;
	vector <int> nums;
	cin >> N;
	int n;
	while (N--) {
		cin >> n;
		nums.push_back(n);
	}
	int scores[2] = { };
	short int turn = 0;
	sort(nums.begin(), nums.end());
	//set<int>::reverse_iterator it = nums.rbegin();
	for (vector <int>::reverse_iterator it = nums.rbegin(); it != nums.rend(); it++) {
		scores[turn] += *it;
		turn = 1 - turn;
	}

	cout << scores[0] << " " << scores[1] << endl;
		
}
