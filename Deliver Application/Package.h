#pragma once

#include <vector>
#include <string>
using namespace std;


class Package {
private:
	string recipient;
	string street;
	int number;
	int yCoord;
	int xCoord;
	bool status;
public:
	Package() { return; }
	Package(string _recipient, string _street, int nr, int _x, int _y, bool _status);
	string getRecipient();
	string getStreet();
	int getNumber();

	void setStatus(bool newStatus);
	bool operator==(pair<pair<int, int>,int> coord);

	int getXCoord();
	int getYCoord();
	bool getStatus();
};

