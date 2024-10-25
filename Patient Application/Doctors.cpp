#include "Doctors.h"

vector<string> Doctors::split(string input, char ch) {
    vector <string> ans;
    stringstream stream(input);
    string buffer;
    while (getline(stream, buffer, ch)) {
        ans.push_back(buffer);
    }

    return ans;
}

void Doctors::readAll() {
    ifstream fin(filename);

    string line;
    while (getline(fin, line)) {
        vector<string> items = split(line, '|');

        Doctor* doc = new Doctor(items[0], items[1], service);
        doctors.push_back(doc);
    }

    fin.close();
}

Doctors::Doctors(string _filename, Service& _service) : filename(_filename), service(_service) {
    readAll();
}

vector<Doctor*> Doctors::getDoctors() {
    return doctors;
}