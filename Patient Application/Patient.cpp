#include "Patient.h"

Patient::Patient() {
	return;
}

Patient::Patient(string _name, string _diagnosis, string _specialisation, string _doctor, string _date) :
	name(_name), diagnosis(_diagnosis), specialisation(_specialisation), doctor(_doctor), date(_date) {}

Patient::Patient(const Patient& p) {
	name = p.name;
	diagnosis = p.diagnosis;
	specialisation = p.specialisation;
	doctor = p.doctor;
	date = p.date;
}

string Patient::getName() {
	return name;
}

string Patient::getDiagnosis() {
	return diagnosis;
}

string Patient::getSpecialisation() {
	return specialisation;
}

string Patient::getDoctor() {
	return doctor;
}

string Patient::getDate() {
	return date;
}

bool Patient::operator==(string _name) {
	return name == _name;
}

void Patient::setDoctor(string newDoctor) {
	doctor = newDoctor;
}

void Patient::setDiagnosis(string newDiagnosis) {
	diagnosis = newDiagnosis;
}

void Patient::setSpecialisation(string newSpecialisation) {
	specialisation = newSpecialisation;
}
