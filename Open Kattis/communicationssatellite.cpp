#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;
int V;
double MSTsum;

double dist(int r1, int x1, int y1, int r2, int x2, int y2) {
	return sqrt( pow(x1 - x2, 2) + pow(y1 - y2, 2) ) - r1 - r2 + 1;
}

int minKey(double key[], bool in_tree[]) {
		double min = 2500;
		int min_index;

		for (int v = 0; v < V; v++) {
			if (in_tree[v] == false && key[v] < min) {
				min = key[v], min_index = v;
			}
		}
		//cout << min_index << " " << min << endl;
		MSTsum += min;
		return min_index;
}
			

void prim(double graph[][2000]) {
	double key[V];
	bool in_tree[V];
	for (int i = 0; i < V; i++) {
		key[i] = 2500, in_tree[i] = false;
	}
	key[0] = 0;
		
	for (int count = 0; count < V; count++ ) {
		int u = minKey(key, in_tree);
		in_tree[u] = true;
		for (int v = 0; v < V; v++) {
			//cout << "graph[" << u << "][" << v << "]: " << graph[u][v] << endl;
			if (graph[u][v] && in_tree[v] == false && graph[u][v] < key[v]) {
				key[v] = graph[u][v];
			}
		}
	}
}



int main() {
	cin >> V;
	
	int sats[V][3];
	int r, x, y;
	double dists[V][2000];

	for (int i = 0; i < V; ++i) {
		cin >> x >> y >> r;
		sats[i][0] = r;
		sats[i][1] = x;
		sats[i][2] = y;
		for (int j = 0; j < i; ++j) {
			dists[i][j] = dists[j][i] = dist(r, x, y,
					sats[j][0], sats[j][1], sats[j][2]);
		}
	}

	prim(dists);

	cout << setprecision(10) << MSTsum - (V - 1) << endl;

	/*
	for (int i = 0; i < V; ++i) {
		for (int j = i + 1; j < V; ++j) {
			cout << dists[i][j] << endl;
		}
	}
	*/

	return 0;

}
