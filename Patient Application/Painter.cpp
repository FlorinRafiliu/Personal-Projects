#include "Painter.h"

Painter::Painter(Service& _service, QWidget* parent) : service(_service), QWidget(parent) {

	ui.setupUi(this);
	service.addObserver(this);
}

void Painter::paintEvent(QPaintEvent* ev) {
	QPainter p{ this };
	p.setPen(Qt::white);

	vector <pair<string, int>> data = service.patientsPerSpec();
	
	int x = 100;
	for (auto i : data) {
		p.drawEllipse(x, 200, i.second * 50, i.second * 50);
		p.drawText(x, 180, QString::fromStdString(i.first));
		x += 200;
	}
}

void Painter::update() { 
	QWidget::update();
}

Painter::~Painter()
{}
