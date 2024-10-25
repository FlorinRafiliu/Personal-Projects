#include "Courier.h"

Courier::Courier(string name, vector<string> streets, pair<pair<int, int>, int> zone, Service& _service, QWidget* parent)
	: CourierName(name), CourierStreets(streets), CourierZone(zone), service(_service), QWidget(parent) {

	ui.setupUi(this);
	
	this->setWindowTitle(QString::fromStdString(CourierName));
	ui.label->setText(QString::fromStdString("Zona: (" + to_string(zone.first.first) + "," + to_string(zone.first.second) + ") - " +
		to_string(zone.second)));
	for (string street : CourierStreets)
		ui.comboBox->addItem(QString::fromStdString(street));

	selected = false;

	service.addObserver(this);
	connections();
	update();
}

void Courier::update() {
	ui.listWidget->clear();
	
	for (Package p : service.getPackages(CourierZone, CourierStreets)) {
		string status;
		if (p.getStatus()) status = "livrat";
		else status = "nelivrat";

		string item = p.getRecipient() + "-" + p.getStreet() + "-" + to_string(p.getNumber()) + "-" +
			to_string(p.getXCoord()) + "-" + to_string(p.getYCoord()) + "-" + status;
		ui.listWidget->addItem(QString::fromStdString(item));
	}

	comboBoxHandler();
}

Courier::~Courier() {}

void Courier::connections() {
	connect(ui.comboBox, &QComboBox::currentIndexChanged,
		this, &Courier::comboBoxHandler);
	connect(ui.deliverPushButton, &QPushButton::clicked,
		this, &Courier::deliverButtonHandler);
	connect(ui.listWidget, &QListWidget::itemSelectionChanged,
		this, &Courier::selectHandler);
}

void Courier::comboBoxHandler() {
	string street = ui.comboBox->currentText().toStdString();

	int row = 0;
	for (Package p : service.getPackages(CourierZone, CourierStreets)) {
		if (p.getStreet() == street || street == "All streets")
			ui.listWidget->item(row)->setHidden(false);
		else
			ui.listWidget->item(row)->setHidden(true);
		row++;
	}
}

void Courier::deliverButtonHandler() {
	if (selected == false) return;
	selected = false;

	int ItemRow = ui.listWidget->currentIndex().row();
	int row = 0;
	for (Package p : service.getPackages(CourierZone, CourierStreets)) {
		if (row == ItemRow) {
			service.deliverPackage(p.getNumber(), p.getXCoord(), p.getYCoord());
			service.notify();
			return ;
		}
		row++;
	}
}

void Courier::selectHandler() {
	selected = true;
}
