#pragma once

#include <QWidget>
#include "ui_CourierCompany.h"
#include "Service.h"
#include <qmessagebox.h>


class CourierCompany : public QWidget, public Observer
{
	Q_OBJECT

public:
	CourierCompany(Service& _service, QWidget *parent = nullptr);
	void update() override;
	~CourierCompany();

private:
	Ui::CourierCompanyClass ui;
	Service& service;

	void connections();
	void addButtonHandler();
};
