#include "Painter.h"


Painter::Painter(Service& _service, vector < pair<pair<int, int>, int> > _couriers, QWidget* parent) 
	: service(_service), couriers(_couriers), QWidget(parent) {
	ui.setupUi(this);

	service.addObserver(this);
	update();
}

void Painter::paintEvent(QPaintEvent* event) {
	vector <Package> data = service.getData();

	QPainter pen{ this };
	pen.setPen(Qt::white);

	for (Package p : data) {
		if (p.getStatus() == false) {
			pen.drawText(p.getXCoord() + 8, p.getYCoord() + 15, QString::number(p.getNumber()));
			pen.drawEllipse(p.getXCoord(), p.getYCoord(), 20, 20);
		}
	}
	pen.setPen(Qt::red);
	for (auto c : couriers) {
		pen.drawEllipse(c.first.first - c.second, c.first.second - c.second, c.second*2, c.second*2);
	}
}

void Painter::update() {
	QWidget::update();
}

Painter::~Painter() {}
