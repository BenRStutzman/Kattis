#include <iostream>



using namespace std;

int main() {
	int W, N;
	cin >> W >> N;
	int a, b;
	int A = 0;
	while (N--) {
		cin >> a >> b;
		A += a * b;
	}
	cout << A / W;	

	return 0;
}
