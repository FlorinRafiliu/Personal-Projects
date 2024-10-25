#pragma once

#include <QWidget>
#include "ui_Painter.h"
#include <vector>
#include <QPainter>
#include "Service.h"
#include "Observer.h"

using namespace std;


class Painter : public QWidget, public Observer
{
	Q_OBJECT

public:
	Painter(Service& _service, QWidget *parent = nullptr);
	void paintEvent(QPaintEvent* ev) override;
	void update() override;
	~Painter();

private:
	Ui::PainterClass ui;
	Service& service;
};
