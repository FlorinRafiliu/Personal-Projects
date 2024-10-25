#pragma once
#include "Doctor.h"
#include "Service.h"


class Doctors {
private:
	vector <Doctor*> doctors;
	Service& service;
	string filename;

	vector <string> split(string input, char ch);
	void readAll();

public:
	Doctors(string _filename, Service& _service);
	vector <Doctor*> getDoctors();
};

