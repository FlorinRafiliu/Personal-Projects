#include "Service.h"
#include "Doctors.h"
#include <QtWidgets/QApplication>
#include "Painter.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
   
    Repository repo("patients.txt");
    Service service(repo);
    
    Doctors doctors("doctors.txt", service);
    
    for (Doctor* doc : doctors.getDoctors())
        doc->show();

    Painter p(service);
    p.show();

    return a.exec();
}
