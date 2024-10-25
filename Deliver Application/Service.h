#pragma once

#include "Repository.h"
#include <algorithm>


class Service {
private:
	Repository& repo;

public:
	Service(Repository& _repo);

	vector <Package> getPackages(pair<pair<int, int>,int> zone, vector <string> streets);
	vector <Package> getData();
	void addPackage(string recipient, string street, int nr, int x, int y);
	void deliverPackage(int number, int x, int y);
	void addObserver(Observer* ob);
	void notify();
};

