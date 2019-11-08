#include <iostream>
#include <string>



using namespace std;

int main() {
	bool found = false;
	string cards [12];
	string card;
	for (int i = 0; i < 12; i++) {
		cin >> card;
		cards[i] = card;
		//cout << card;
	}
	bool match;
	for (int i = 0; i < 12; i++) {
		for (int j = i + 1; j < 12; j++) {
			for (int k = j + 1; k < 12; k++) {
				match = true;
				for (int m = 0; m < 4; m++) {
					if (!((cards[i][m] == cards[j][m] &&
						cards[j][m] == cards[k][m]) |
						(cards[i][m] != cards[j][m] &&
						cards[j][m] != cards[k][m] &&
						cards[i][m] != cards[k][m]))) {
						match = false;
						break;
					}
				}
				if (match) {
					found = true;
					cout << i + 1 << " " << j + 1
					<< " " << k + 1 << endl;			
				}
			}
		}
	}

	if (!found) cout << "no sets" << endl;

	return 0;
}
