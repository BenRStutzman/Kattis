#include <iostream>
#include <string>

using namespace std;

int main() {
	string game_record;
	cin >> game_record;

	cout << game_record[game_record.length() - 2] << endl;
	
	return 0;
}
