#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	string message;
	cin >> message;
	int N = message.size();
	int len = N * 4 + 1;
	vector <vector <char> > output;
	char now;
	vector <char> row;
	for (int i = 0; i < len; ++i) {
		if (i % 4 == 2) {
			if ((i / 4) % 3 == 2) now = '*';
			else now = '#';
		} else now = '.';
		row.push_back(now);
	}
	output.push_back(row);
	output.push_back(row);
	row.clear();
	for (int i = 0; i < len; ++i) {
		if (i % 2 == 1) {
			if ((i / 4) % 3 == 2) now = '*';
			else now = '#';
		} else now = '.';
		row.push_back(now);
	}
	output.insert(output.begin() + 1, row);
	output.insert(output.begin() + 1, row);
	row = {'#'};
	for (int i = 1; i < len; ++i) {
		if (i % 2 == 0) {
			if (i % 4 == 2) now = message[i / 4];
			else {
				if (i % 12 == 0) now = '*';
				else if (i % 12 == 8) {
					if (i == len - 1) now = '#';
					else now = '*';
				} else {
					now = '#';
				}
			}
		} else now = '.';
		row.push_back(now);
	}
	output.insert(output.begin() + 2, row);	

	for (auto line : output) {
		for (auto symbol : line) {
			cout << symbol;
		}
		cout << endl;
	}	

	return 0;
}
