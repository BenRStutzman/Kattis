#include <set>
#include <vector>
#include <iostream>
using namespace std;

set <int> untried;
vector <int> color_arr;
vector < set <int> > graph;
int N, M, node;
bool odd;
int components;


bool find_odd() {
	color_arr[node] = 1;
	vector <int> q;
	q.push_back(node);
		
	while (!q.empty()) {
		int u = q.back();
		q.pop_back();
		untried.erase(u);

		for (set <int> :: iterator it = graph[u].begin(); it != graph[u].end();
				it++) {
			if (color_arr[*it]) {
				if (color_arr[*it] == color_arr[u]) {
					odd = true;
				}
			} else {   
				color_arr[*it] = -color_arr[u];
				q.push_back(*it);
			}
		}
	}
	return odd;
}

int main() {
	
	cin >> N >> M;

	graph = vector < set <int> > (N);
	color_arr = vector <int> (N, 0);	

	for (int i =0; i < N; i++) {
		untried.insert(i);
	}

	int A, B;
	while (M--) {
		cin >> A >> B;
		//cerr << "A: " << A << "B: " << B << endl;;
		graph[A - 1].insert(B - 1);
		graph[B - 1].insert(A - 1);
	}
	
	while (!untried.empty()) {
		node = 	*untried.begin();
	
		if (find_odd()) {
			odd = true;
		}
		components ++;
	}

	if (odd) {
		cout << components - 1 << endl;
	} else {
		cout << components << endl;
	}
	
	return 0;
}

