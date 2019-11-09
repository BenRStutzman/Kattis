#include <iostream>
#include <string>

using namespace std;

char octal(char a, char b, char c) {
	string bin = "";
	bin += a;
	bin += b;
	bin += c;
	//cout << "bin: " << bin << endl;
	int bin_num = stoi(bin);
	//cout << "bin_num: " << bin_num << endl;
	switch (bin_num) {
		case (0): return '0';
		case (1): return '1';
		case (10): return '2';
		case (11): return '3';
		case (100): return '4';
		case (101): return '5';
		case (110): return '6';
		case (111): return '7';
		default: return '8';
	}
}

int main() {
	string line;
	getline(cin, line);
	for (int i = 0; i < (line.size() % 3); i++) {
		line = "0" + line;
	}
	//cout << line;
	string output;
	char a, b, c;
	for (int i = 0; i < line.size(); i += 3) {
		a = line[i];
		b = line[i + 1];
		c = line[i + 2];
		//cout << a << " " << b << " " << c << endl;
		output += octal(a, b, c);
	}
	cout << output << endl;
	return 0;
}
