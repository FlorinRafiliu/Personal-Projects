#include "Package.h"

Package::Package(string _recipient, string _street, int nr, int _x, int _y, bool _status) :
	recipient(_recipient), street(_street), number(nr), xCoord(_x), yCoord(_y), status(_status) {}

string Package::getRecipient() {
	return recipient;
}

string Package::getStreet() {
	return street;
}

int Package::getNumber() {
	return number;
}

void Package::setStatus(bool newStatus) {
	status = newStatus;
}

bool Package::operator==(pair<pair<int, int>,int> coord) {
	return xCoord == coord.first.first && yCoord == coord.first.second && number == coord.second;
}

int Package::getXCoord() {
	return xCoord;
}

int Package::getYCoord() {
	return yCoord;
}

bool Package::getStatus() {
	return status;
}
