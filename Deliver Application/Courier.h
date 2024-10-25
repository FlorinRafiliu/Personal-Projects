#pragma once

#include <QWidget>
#include "ui_Courier.h"
#include "Service.h"


class Courier : public QWidget, public Observer
{
	Q_OBJECT

public:
	Courier(string name, vector<string> streets, pair<pair<int, int>, int> zone, Service& _service, QWidget *parent = nullptr);
	void update() override;
	~Courier();

private:
	Ui::CourierClass ui;
	Service& service;
	string CourierName;
	vector <string> CourierStreets;
	pair<pair<int, int>, int> CourierZone;

	bool selected;

	void connections();
	void comboBoxHandler();
	void deliverButtonHandler();
	void selectHandler();
};
