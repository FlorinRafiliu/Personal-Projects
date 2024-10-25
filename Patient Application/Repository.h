#pragma once
#include "Observer.h"
#include "Patient.h"
#include <fstream>
#include <sstream>


class Repository : public Observable {
private:
	vector <Patient> data;
	string filename;

	vector <string> split(string input, char ch);
	void readAll();
	void writeAll();

public:
	Repository(string _filename);

	vector <Patient> getData();
	void addPatient(Patient p);
	void updatePatient(string name, string newDiagnosis, string newSpecialisation, string newDoc);
};

