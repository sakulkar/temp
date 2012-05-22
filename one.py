#!/usr/bin/python

#this is just test file

class Employee:
    'Common base class for all employees'
    count = 0;

    def __init__(self,name,salary):
        self.name = name;
	self.salary = salary;
	Employee.count = Employee.count + 1;

    def displayCount(self):
	print "total number of employees", Employee.count;

    def displayProfile(self):
	print "name =", self.name, "/n salary", self.salary;

"execution starts from here"
emp1 = Employee("Praveen",12000);
emp2 = Employee("Radha",23000);
emp1.displayProfile();
emp2.displayCount();
#Employee.displayCount();
