#pragma once
#include "Dog.h"


class Validator {
public:
	Validator() = default;
	bool validateDog(Dog&);
	bool validatePhoto(const string&);
};

