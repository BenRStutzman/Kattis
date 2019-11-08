#include <set>
#include <vector>
#include <iostream>
using namespace std;


void add_to_comp(int &node, set <int> &left, vector <set <int> > &graph,
				set <int> &group, int &n) {
	//cerr << node << endl;
	//set<int> iterator it = graph[node].begin();
	bool found_new = false;
	for (set <int>::iterator it = graph[node].begin(); it != graph[node].end(); it++) {
		if (left.count(*it)) {
			left.erase(*it);
			group.insert(*it);
			found_new = true;
		}
	}
	group.erase(node);          
}


bool find_odd(vector <set <int> > &graph, int &node, int &N, vector <int>
				&color_arr) {
	color_arr[node] = 1;
	vector <int> q;
	q.push_back(node);
		
	while (!q.empty()) {
		int u = q.back();
		q.pop_back();

		for (int v = 0; v < N; v++) {
			if (graph[u].count(v)) {
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
	vector < set <int> > graph(N);
	int A, B;
	while (M--) {
		cin >> A >> B;
		//cerr << "A: " << A << "B: " << B << endl;;
		graph[A - 1].insert(B - 1);
		graph[B - 1].insert(A - 1);
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
		left.erase(node);
		set <int> group;
		group.insert(node); 
		while (!group.empty()) {
			node = *group.begin();
			add_to_comp(node, left, graph, group, N);
		}
		//cout << node << endl;
		components.push_back(node);
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

