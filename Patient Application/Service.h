#pragma once
#include "Repository.h"
#include <algorithm>
#include <map>

class Service {
private:
	Repository& repo;
public:
	Service(Repository& _repo);
	
	void addPatient(string _name, string _diagnosis, string _specialisation, string _doctor, string _date);
	void updatePatient(string name, string newDiagnosis, string newSpecialisation, string newDoc);
	
	vector <pair<string, int>> patientsPerSpec();

	vector <Patient> getData();
	vector <Patient> getDataBySpec(string specialisation);

	void notify();
	void addObserver(Observer* observer);
};

