#include "Repo.h"
#include "Service.h"
#include "ServiceUser.h"
#include "Tests.h"
#include "FileRepository.h"
#include <iostream>
#include "SaveCsv.h"
#include "SaveHtml.h"

#include <qapplication.h>
#include "ModeGUI1.h"

using namespace std;

int main(int argc, char* argv[]) {
	QApplication application(argc, argv);

	allTests();

	FileRepository repo("input.txt");
	Validator val;
	Service service(repo, val);

	Repository adoptionList;
	ServiceUser serviceUser(repo, adoptionList);

	ModeGUI1 modeGui(service, serviceUser);
	modeGui.show();
	
	return application.exec();
}