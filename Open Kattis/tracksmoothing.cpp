#include <iostream>
#include <cmath>
#define PI 3.14159265358979323846264338327950288419716939937510582

using namespace std;

double dist(int x0, int y0, int x1, int y1) {
	return sqrt((x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1));
}


int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int R, V;
		
		double total_dist = 0;
		
		cin >> R >> V;
		int x_0, y_0;
		cin >> x_0 >> y_0;
		int x0 = x_0;
		int y0 = y_0;
		int x, y;
		for (int i = 0; i < V - 1; i++) {
			cin >> x >> y;
			total_dist += dist(x0, y0, x, y);
			x0 = x;
			y0 = y;
		}
		total_dist += dist(x_0, y_0, x, y);
		double s = (total_dist - 2 * PI * R) / total_dist;
		if (s < 0) {
			cout << "Not possible" << endl;

		} else {
			cout << s << endl;
		}
	}
	return 0;
}

		

		
		

