#pragma once

#include <vector>
using namespace std;


class Observer {
public:
	virtual void update() = 0;
};

class Observable {
private:
	vector <Observer*> observers;
public:
	
	void addObserver(Observer* observer) {
		observers.push_back(observer);
	}

	void notify() {
		for (Observer* observer : observers) {
			observer->update();
		}
	}
};

