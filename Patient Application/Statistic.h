#pragma once

#include <QMainWindow>
#include "ui_Statistic.h"

class Statistic : public QMainWindow
{
	Q_OBJECT

public:
	Statistic(QWidget *parent = nullptr);
	~Statistic();

private:
	Ui::StatisticClass ui;
};
