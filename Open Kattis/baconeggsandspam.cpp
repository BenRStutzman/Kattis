#include <iostream>
#include <set>
#include <string>
#include <sstream>
#include <map>
#include <iterator>
#include <vector>

using namespace std;

template <typename Out>
void split(const string &s, char delim, Out result) {
    istringstream iss(s);
    string item;
    while (getline(iss, item, delim)) {
        *result++ = item;
    }
}
vector <string> split(const string &s, char delim) {
    vector<string> elems;
    split(s, delim, back_inserter(elems));
    return elems;
}

int main() {
	map <string, set <string> > items;

	string line;
	getline(cin, line);
	int N = stoi(line);
	vector <string> words;
	while (N) {
		for (int i = 0; i < N; ++i) {

			getline(cin, line);
			vector <string> words = split(line, ' ');
			for (string s : vector <string> (words.begin() + 1, words.end())) {
				items[s].insert(words[0]);
			}
		}
		for (auto x : items) {
			cout << x.first ;
			for (string person : x.second) {
				cout << " " << person;
			}
			cout << endl;
		}
		items.clear();
		getline(cin, line);
		N = stoi(line);
		if (N) cout << endl;
	}	
		

	return 0;
}
