#include <QtWidgets/QApplication>
#include "Couriers.h"
#include "CourierCompany.h"
#include "Painter.h"


int main(int argc, char *argv[]) {
    QApplication a(argc, argv);

    Repository repo("pachete.txt");
    Service service(repo);
    Couriers couriers("curieri.txt", service);
    
    for (Courier* c : couriers.getCouriers())
        c->show();

    CourierCompany company(service);
    company.show();

    Painter p(service, couriers.getInfo());
    p.show();

    return a.exec();
}
