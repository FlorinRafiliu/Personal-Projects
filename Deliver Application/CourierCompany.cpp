#include "CourierCompany.h"


CourierCompany::CourierCompany(Service& _service, QWidget* parent) : service(_service), QWidget(parent) {
	ui.setupUi(this);

	service.addObserver(this);
	update();
	connections();
}

void CourierCompany::update() {
	ui.listWidget->clear();
	int row = 0;
	for (Package p : service.getData()) {
		string item = p.getRecipient() + "-" + p.getStreet() + "-" + to_string(p.getNumber()) + "-" +
			to_string(p.getXCoord()) + "-" + to_string(p.getYCoord());
		ui.listWidget->addItem(QString::fromStdString(item));
		if (p.getStatus())
			ui.listWidget->item(row)->setBackground(Qt::green);
		row++;
	}
}

CourierCompany::~CourierCompany() {}

void CourierCompany::connections() {
	connect(ui.addButton, &QPushButton::clicked,
		this, &CourierCompany::addButtonHandler);
}

void CourierCompany::addButtonHandler() {
	if(ui.recipientLineEdit->text().isEmpty() || ui.streetLineEdit->text().isEmpty() || ui.numberLineEdit->text().isEmpty() ||
	   ui.xLineEdit->text().isEmpty() || ui.yLineEdit->text().isEmpty())
	{ 
		QMessageBox* q = new QMessageBox();
		q->show();
		return;
	}

	string recipient = ui.recipientLineEdit->text().toStdString();
	string street = ui.streetLineEdit->text().toStdString();
	int number = stoi(ui.numberLineEdit->text().toStdString());
	int x = stoi(ui.xLineEdit->text().toStdString());
	int y = stoi(ui.yLineEdit->text().toStdString());

	service.addPackage(recipient, street, number, x, y);
	service.notify();
}
