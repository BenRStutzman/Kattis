#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector <int> turns (int n) {
	vector <int> right_turns;
	while (n > 1) {
		right_turns.push_back(n % 2);
		n /= 2;
	}
	return right_turns;
}

void make_frac (int &num, int &den, vector <int> right_turns) {
	for (vector <int>::reverse_iterator it = right_turns.rbegin(); it != right_turns.rend(); ++it) {
		if (*it) num += den;
		else den += num;
	}
}
		

int main() {
	int N;
	cin >> N;
	int x, n, num, den;
	while (N--) {
		cin >> x >> n;
		//cout << n << endl;
		num = den = 1;
		make_frac(num, den, turns(n));
		cout << x << " " << num << "/" << den << endl;
	}
		
	return 0;
}	
