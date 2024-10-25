#pragma once

#include <QWidget>
#include "ui_Painter.h"
#include "Service.h"
#include <qpainter.h>


class Painter : public QWidget, public Observer
{
	Q_OBJECT

public:
	Painter(Service& _service, vector < pair<pair<int, int>, int> > _couriers, QWidget *parent = nullptr);
	void paintEvent(QPaintEvent* event) override;
	void update() override;
	~Painter();

private:
	Ui::PainterClass ui;
	Service& service;
	vector < pair<pair<int, int>, int> > couriers;
};
