#include <iostream>
#include <vector>

using namespace std;

bool is_attacked(int A, int B, int X) {
	return ((X - 1) % (A + B) < A);
}

int main() {
	int A, B, C, D, X, Y, Z;
	cin >> A >> B >> C >> D >> X >> Y >> Z;
	int people [] = {X, Y, Z};
	int attacks;
	for (int person : people) {
		attacks = 0;
		if (is_attacked(A, B, person)) attacks++;
		if (is_attacked(C, D, person)) attacks++;
		switch (attacks) {
			case 0:
				cout << "none" << endl;
				break;
			case 1:
				cout << "one" << endl;
				break;
			case 2:
				cout << "both" << endl;
				break;
		}
	}
	return 0;
}	
