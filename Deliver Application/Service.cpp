#include "Service.h"

Service::Service(Repository& _repo) : repo(_repo) {}

vector<Package> Service::getPackages(pair<pair<int, int>, int> zone, vector<string> streets) {
	vector <Package> data = repo.getData();
	vector <Package> newData(data.size());

	int x = zone.first.first;
	int y = zone.first.second;
	int r = zone.second;

	auto it = copy_if(data.begin(), data.end(), newData.begin(),
		[x, y, r, streets](Package& p) {
			if (p.getStatus()) return false;
			int distance = abs(x - p.getXCoord()) * abs(x - p.getXCoord()) +
						   abs(y - p.getYCoord()) * abs(y - p.getYCoord());
			if (distance <= r * r)
				return true;
			
			return find(streets.begin(), streets.end(), p.getStreet()) != streets.end();
		});

	newData.resize(distance(newData.begin(), it));

	return newData;
}

vector<Package> Service::getData() {
	return repo.getData();
}

void Service::addPackage(string recipient, string street, int nr, int x, int y) {
	Package p(recipient, street, nr, x, y, false);
	repo.addPackage(p);
}

void Service::deliverPackage(int number, int x, int y) {
	repo.deliver(number, x, y);
}

void Service::addObserver(Observer* ob) {
	repo.addObserver(ob);
}

void Service::notify() {
	repo.notify();
}
