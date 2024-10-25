#include "Service.h"

Service::Service(Repository& _repo) : repo(_repo) {}

void Service::addPatient(string _name, string _diagnosis, string _specialisation, string _doctor, string _date) {
	Patient p(_name, _diagnosis, _specialisation, _doctor, _date);
	repo.addPatient(p);
}

void Service::updatePatient(string name, string newDiagnosis, string newSpecialisation, string newDoc) {
	repo.updatePatient(name, newDiagnosis, newSpecialisation, newDoc);
}

vector<pair<string, int>> Service::patientsPerSpec() {
	vector <pair<string, int>> ans;
	
	map <string, int> M;
	
	vector <Patient> data = repo.getData();
	for (Patient p : data) {
		if (p.getSpecialisation() == "")
			M["undiagnosed"] += 1;
		else 
			M[p.getSpecialisation()] += 1;
	}

	for (auto i : M) {
		ans.push_back({ i.first, i.second });
	}

	return ans;
}

vector<Patient> Service::getData() {
	return repo.getData();
}

vector<Patient> Service::getDataBySpec(string specialisation) {
	vector<Patient> data = repo.getData();
	vector <Patient> newData(data.size());
	
	auto it = copy_if(data.begin(), data.end(), newData.begin(),
		[specialisation](Patient& p) {
			return p.getSpecialisation() == specialisation || p.getDiagnosis() == "undiagnosed";
		});

	newData.resize(distance(newData.begin(), it));
	sort(newData.begin(), newData.end(),
		[](Patient& a, Patient& b) {
			return a.getDate() < b.getDate();
		});
	
	return newData;
}

void Service::notify() {
	repo.notify();
}

void Service::addObserver(Observer* observer) {
	repo.addObserver(observer);
}
