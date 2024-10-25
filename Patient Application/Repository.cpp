#include "Repository.h"

vector<string> Repository::split(string input, char ch) {
    vector <string> ans;
    stringstream stream(input);
    string buffer;
    while (getline(stream, buffer, ch)) {
        ans.push_back(buffer);
    }

    return ans;
}

void Repository::readAll() {
    ifstream fin(filename);

    data.clear();

    string line;
    while (getline(fin, line)) {
        vector<string> items = split(line, '|');

        Patient p(items[0], items[1], items[2], items[3], items[4]);
        data.push_back(p);
    }

    fin.close();
}

void Repository::writeAll() {
    ofstream fout(filename);

    for (Patient p : data) {
        fout << p.getName() << "|";
        fout << p.getDiagnosis() << "|";
        fout << p.getSpecialisation() << "|";
        fout << p.getDoctor() << "|";
        fout << p.getDate() << "\n";
    }

    fout.close();
}

Repository::Repository(string _filename) : filename(_filename) {
    readAll();
}

vector<Patient> Repository::getData() {
    return data;
}

void Repository::addPatient(Patient p) {
    readAll();
    data.push_back(p);
    writeAll();
}

void Repository::updatePatient(string name, string newDiagnosis, string newSpecialisation, string newDoc) {
    readAll();
    auto it = find(data.begin(), data.end(), name);
    it->setDiagnosis(newDiagnosis);
    it->setSpecialisation(newSpecialisation);
    it->setDoctor(newDoc);
    writeAll();
}
