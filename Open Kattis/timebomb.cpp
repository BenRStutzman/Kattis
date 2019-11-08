#include <iostream>
#include <vector>

using namespace std;

bool equals(char input[5][3], char ASCII[5][3]) {
	for (int i = 0; i < 5; ++i) {
		for (int j = 0; j < 3; ++j) {
			if (input[i][j] != ASCII[i][j]) return false;
		}
	}
	return true;
}

int eval_ASCII(char ASCII[5][3]) {
	char A [5][3] = {{'*', '*', '*'},
			   {'*', ' ', '*'},
			   {'*', ' ', '*'},
			   {'*', ' ', '*'},
			   {'*', '*', '*'}};
	char B [5][3] = {{' ', ' ', '*'},
			   {' ', ' ', '*'},
			   {' ', ' ', '*'},
			   {' ', ' ', '*'},
			   {' ', ' ', '*'}};
	char C [5][3] = {{'*', '*', '*'},
			   {' ', ' ', '*'},
			   {'*', '*', '*'},
			   {'*', ' ', ' '},
			   {'*', '*', '*'}};		
	char D [5][3] = {{'*', '*', '*'},
			   {' ', ' ', '*'},
			   {'*', '*', '*'},
			   {' ', ' ', '*'},
			   {'*', '*', '*'}};
	char E [5][3] = {{'*', ' ', '*'},
			   {'*', ' ', '*'},
			   {'*', '*', '*'},
			   {' ', ' ', '*'},
			   {' ', ' ', '*'}};
	char F [5][3] = {{'*', '*', '*'},
			   {'*', ' ', ' '},
			   {'*', '*', '*'},
			   {' ', ' ', '*'},
			   {'*', '*', '*'}};
	char G [5][3] = {{'*', '*', '*'},
			   {'*', ' ', ' '},
			   {'*', '*', '*'},
			   {'*', ' ', '*'},
			   {'*', '*', '*'}};
	char H [5][3] = {{'*', '*', '*'},
			   {' ', ' ', '*'},
			   {' ', ' ', '*'},
			   {' ', ' ', '*'},
			   {' ', ' ', '*'}};
	char I [5][3] = {{'*', '*', '*'},
			   {'*', ' ', '*'},
			   {'*', '*', '*'},
			   {'*', ' ', '*'},
			   {'*', '*', '*'}};
	char J [5][3] = {{'*', '*', '*'},
			   {'*', ' ', '*'},
			   {'*', '*', '*'},
			   {' ', ' ', '*'},
			   {'*', '*', '*'}};

	if (equals(ASCII, A)) return 0;
	else if (equals(ASCII, B)) return 1;
	else if (equals(ASCII, C)) return 2;
	else if (equals(ASCII, D)) return 3;
	else if (equals(ASCII, E)) return 4;
	else if (equals(ASCII, F)) return 5;
	else if (equals(ASCII, G)) return 6;
	else if (equals(ASCII, H)) return 7;
	else if (equals(ASCII, I)) return 8;
	else if (equals(ASCII, J)) return 9;
	else return -1;


}


int main() {
	string line;
	getline(cin, line);
	vector <char [5][3] > letters (line.size() / 4 + 1);
		for (int j = 0; j < line.size(); j++) {
			if (j % 4 != 3) {
				//cout << j << endl;
				//cout << line[j] << endl;
				letters[j / 4][0][j % 4] = line[j];
			}
		}

	for (int i = 1; i < 5; ++i) {
		getline(cin, line);
		for (int j = 0; j < line.size(); j++) {
			if (j % 4 != 3) {
				letters[j / 4][i][j % 4] = line[j];
			}
		}
	}

	int total = 0;
	int num;
	for (vector <char [5][3] >::iterator it = letters.begin();
		it != letters.end(); ++it) {
		num = eval_ASCII(*it);
		if (num >= 0) {
			//cout << num << endl;
			total = total * 10 + num;
		} else {
			//cout << num << endl;
			cout << "BOOM!!" << endl;
			return 0;
		}
	}
	//cout << total << endl;
	if (total % 6 == 0) {
		cout << "BEER!!" << endl;
	} else { cout << "BOOM!!" << endl;
		}

	return 0;
}	
