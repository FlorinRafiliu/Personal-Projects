#pragma once

#include "Observer.h"
#include "Package.h"
#include <fstream>
#include <sstream>
#include <algorithm>


class Repository : public Observable {
private:
	vector <Package> data;
	string filename;

	vector <string> split(string input, char ch);
	void readAll();
	void writeAll();

public:
	Repository(string _filename);

	void deliver(int nr, int x, int y);
	void addPackage(Package p);
	vector <Package> getData();
};

