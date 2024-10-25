#pragma once

#include <QWidget>
#include "ui_Doctor.h"
#include "Service.h"
#include "Observer.h"
#include <qcheckbox.h>
#include <qmessagebox.h>


class Doctor : public QWidget, public Observer
{
	Q_OBJECT

public:
	Doctor(string _name, string _specialisation, Service& _service, QWidget *parent = nullptr);
	void update() override;
	~Doctor();

private:
	Ui::DoctorClass ui;
	Service& service;
	string DoctorName;
	string DoctorSpecialisation;

	void connections();
	void myPatientsButtonHandler();
	void addButtonHandler();
	void updateButtonHandler();
	void selectedRowHandler();

};
