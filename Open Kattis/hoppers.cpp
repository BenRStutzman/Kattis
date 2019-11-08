#include <set>
#include <vector>
#include <iostream>
using namespace std;


void add_to_comp(int &node, set <int> &left, vector <vector <int> > &graph,
				set <int> &group, int &N) {
	for (int i = 0; i < N; i++) {
		if (graph[node][i]) {
			//cerr << node << i << endl;
			left.erase(i);
			if (group.count(i) == 0) {
				group.insert(i);
				add_to_comp(i, left, graph, group, N);
			}
		}
	}                 
}


bool find_odd(vector <vector <int> > &graph, int &node, int &N, vector <int>
				&color_arr) {
	color_arr[node] = 1;
	vector <int> q;
	q.push_back(node);
		
	while (!q.empty()) {
		int u = q.back();
		q.pop_back();

		for (int v = 0; v < N; v++) {
			if (graph[u][v]) {
				if (color_arr[v] == -1) {   
					color_arr[v] = 1 - color_arr[u];
					q.push_back(v);
				} else if (color_arr[v] == color_arr[u]) {
					return true;
				}
			}
		}
	}
	return false;
}

int main() {
	int N, M;
	cin >> N >> M;
	vector < vector <int> > graph(N, vector <int> (N));
	int A, B;
	while (M--) {
		cin >> A >> B;
		//cerr << "A: " << A << "B: " << B << endl;;
		graph[A - 1][B - 1] = graph[B - 1][A - 1] = 1;
	}

	/*
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << graph[i][j];
		}
	cout << endl;
	}
	*/

	set <int> left;
	vector <int> color_arr;
	for (int i =0; i < N; i++) {
		left.insert(i);
		color_arr.push_back(-1);
	}
	
	vector <int> components;

	int node;
	while (!left.empty()) {
		node = *left.begin();
		left.erase(left.begin());
		set <int> group;
		group.insert(node); 
		add_to_comp(node, left, graph, group, N);
		//cout << node << endl;
		components.push_back(*group.begin());
	}
	for (int i = 0; i < components.size(); i++) {
		if (find_odd(graph, components[i], N, color_arr)) {
			cout << components.size() - 1 << endl;
			return 0;
		}
	}
	cout << components.size() << endl;	
	return 0;
}

