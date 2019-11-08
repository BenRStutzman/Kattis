#include <iostream>
#include <string>
#include <set>



using namespace std;

int main() {

	set <string> in;
	set <string> out;

	int N;
	cin >> N;
	string person;
	string action;

	while (N--) {
		cin >> action >> person;
		cout << person;
		if (action == "entry") {
			cout << " entered";
			if (in.count(person)) {
				cout << " (ANOMALY)";
			} else in.insert(person);
			cout << endl;
			out.erase(person);
		} else {
			cout << " exited";
			if (in.count(person) == 0) {
				cout << " (ANOMALY)";
			} else out.insert(person);
			cout << endl;
			in.erase(person);
		}
	}

	return 0;
}
