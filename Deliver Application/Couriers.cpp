#include "Couriers.h"

vector<string> Couriers::split(string input, char ch) {
    vector <string> ans;
    stringstream stream(input);
    string buffer;
    while (getline(stream, buffer, ch)) {
        ans.push_back(buffer);
    }

    return ans;
}

void Couriers::readAll() {
    ifstream fin(filename);

    string line;
    while (getline(fin, line)) {
        vector <string> items = split(line, '|');
        vector <string> streets = split(items[1], ',');

        int x = stoi(items[2]);
        int y = stoi(items[3]);
        int r = stoi(items[4]);

        Courier* c = new Courier(items[0], streets, { {x, y}, r }, service);
        couriersInfo.push_back({ {x, y}, r });
        couriers.push_back(c);
    }

    fin.close();
}

Couriers::Couriers(string _filename, Service& _service) : filename(_filename), service(_service) {
    readAll();
}

vector<Courier*> Couriers::getCouriers() {
    return couriers;
}

vector<pair<pair<int, int>, int>> Couriers::getInfo() {
    return couriersInfo;
}
