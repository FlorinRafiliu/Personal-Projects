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
        vector <string> items = split(line, '|');
        
        bool status;
        if (items[5] == "false")
            status = false;
        else
            status = true;

        Package p(items[0], items[1], stoi(items[2]), stoi(items[3]), stoi(items[4]), status);
        data.push_back(p);
    }

    fin.close();
}

void Repository::writeAll() {
    ofstream fout(filename);

    for (Package p : data) {
        fout << p.getRecipient() << "|";
        fout << p.getStreet() << "|";
        fout << p.getNumber() << "|";
        fout << p.getXCoord() << "|";
        fout << p.getYCoord() << "|";
        if (p.getStatus())
            fout << "true\n";
        else
            fout << "false\n";
    }

    fout.close();
}

Repository::Repository(string _filename) : filename(_filename) {
    readAll();
}

void Repository::deliver(int nr, int x, int y) {
    readAll();
    auto it = find(data.begin(), data.end(), make_pair(make_pair(x,y),nr));
    it->setStatus(true);
    writeAll();
}

void Repository::addPackage(Package p) {
    readAll();
    data.push_back(p);
    writeAll();
}

vector<Package> Repository::getData() {
    return data;
}
