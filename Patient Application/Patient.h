#pragma once

#include <string>
using namespace std;


class Patient {
private:
	string name;
	string diagnosis;
	string specialisation;
	string doctor;
	string date;

public:
	Patient();
	Patient(string _name, string _diagnosis, string _specialisation, string _doctor, string _date);
	Patient(const Patient& p);
	string getName();
	string getDiagnosis();
	string getSpecialisation();
	string getDoctor();
	string getDate();

	bool operator==(string _name);

	void setDoctor(string newDoctor);
	void setDiagnosis(string newDiagnosis);
	void setSpecialisation(string newSpecialisation);
};

