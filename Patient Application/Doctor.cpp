#include "Doctor.h"


Doctor::Doctor(string _name, string _specialisation, Service& _service, QWidget* parent)
	: DoctorName(_name), DoctorSpecialisation(_specialisation), service(_service), QWidget(parent) {
	
	ui.setupUi(this);

	this->setWindowTitle(QString::fromStdString(DoctorName));
	service.addObserver(this);

	ui.updateNameLineEdit->setReadOnly(true);
	ui.updateDoctorLineEdit->setReadOnly(true);
	ui.updateDateLineEdit->setReadOnly(true);

	connections();
	update();
}

void Doctor::update() {
	vector <Patient> data = service.getDataBySpec(DoctorSpecialisation);

	ui.patientTableWidget->clear();
	ui.patientTableWidget->setRowCount(data.size());
	ui.patientTableWidget->setColumnCount(5);

	int row = 0;
	for (Patient p : data) {
		ui.patientTableWidget->setItem(row, 0, new QTableWidgetItem(QString::fromStdString(p.getName())));
		ui.patientTableWidget->setItem(row, 1, new QTableWidgetItem(QString::fromStdString(p.getDiagnosis())));
		ui.patientTableWidget->setItem(row, 2, new QTableWidgetItem(QString::fromStdString(p.getSpecialisation())));
		ui.patientTableWidget->setItem(row, 3, new QTableWidgetItem(QString::fromStdString(p.getDoctor())));
		ui.patientTableWidget->setItem(row, 4, new QTableWidgetItem(QString::fromStdString(p.getDate())));
		
		if (p.getDoctor() == DoctorName) {
			ui.patientTableWidget->item(row, 0)->setBackground(Qt::green);
			ui.patientTableWidget->item(row, 1)->setBackground(Qt::green);
			ui.patientTableWidget->item(row, 2)->setBackground(Qt::green);
			ui.patientTableWidget->item(row, 3)->setBackground(Qt::green);
			ui.patientTableWidget->item(row, 4)->setBackground(Qt::green);
		}

		row++;
	}
}

Doctor::~Doctor() {}

void Doctor::connections() {
	connect(ui.patientBox, &QCheckBox::checkStateChanged,
		this, &Doctor::myPatientsButtonHandler);
	connect(ui.addButton, &QPushButton::clicked,
		this, &Doctor::addButtonHandler);
	connect(ui.updateButton, &QPushButton::clicked,
		this, &Doctor::updateButtonHandler);
	connect(ui.patientTableWidget, &QTableWidget::itemChanged,
		this, &Doctor::selectedRowHandler);
}

void Doctor::myPatientsButtonHandler() {
	if (ui.patientBox->isChecked()) {
		for (int i = 0; i < ui.patientTableWidget->rowCount(); i++) {
			if(ui.patientTableWidget->item(i, 3)->text().toStdString() != DoctorName)
			ui.patientTableWidget->hideRow(i);
		}
	}
	else {
		for (int i = 0; i < ui.patientTableWidget->rowCount(); i++) {
			ui.patientTableWidget->showRow(i);
		}
	}
}

void Doctor::addButtonHandler() {
	if (ui.nameLineEdit->text().isEmpty() || ui.dateLineEdit->text().toStdString() <= "2024-06-26") {
		QMessageBox* q = new QMessageBox();
		q->show();
		return;
	}

	string name = ui.nameLineEdit->text().toStdString();
	string diagnosis = ui.diagnosisLineEdit->text().toStdString();
	string specialisation = ui.specialisationLineEdit->text().toStdString();
	string doctor = ui.doctorLineEdit->text().toStdString();
	string date = ui.dateLineEdit->text().toStdString();

	if (diagnosis == "") diagnosis = "undiagnosed";

	service.addPatient(name, diagnosis, specialisation, doctor, date);
	service.notify();
}

void Doctor::updateButtonHandler() {
	if (ui.updateDiagnosisLineEdit->text().toStdString() == "undiagnosed" ||
		ui.updateDoctorLineEdit->text().toStdString() == DoctorName) {

		string name = ui.nameLineEdit->text().toStdString();
		string diagnosis = ui.updateDiagnosisLineEdit->text().toStdString();
		string specialisation = ui.updateSpecialisationLineEdit->text().toStdString();
		string doctor = "";
		string date = ui.updateDateLineEdit->text().toStdString();

		service.updatePatient(name, diagnosis, specialisation, doctor);
		service.notify();
	}
}

void Doctor::selectedRowHandler() {
	int row = ui.patientTableWidget->currentRow();

}
