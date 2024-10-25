#pragma once

#include "Service.h"
#include "Courier.h"


class Couriers {
private:
	Service& service;
	vector <Courier*> couriers;
	string filename;
	vector < pair<pair<int, int>, int> > couriersInfo;

	vector <string> split(string input, char ch);
	void readAll();

public:
	Couriers(string _filename, Service& _service);
	vector <Courier*> getCouriers();
	vector < pair<pair<int, int>, int> > getInfo();
};

