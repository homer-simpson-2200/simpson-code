#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main() {
  //c-string
  //char name_DB[] = {'H', 'o', 'm', 'e', 'r', '\0'}; //c-string doesn't recommend, '\0' means that the variable is string. if c-string variable doesn't contain '\0', it is not a string. it's array.
	//char name;
	//char ps[5]; // can save 5 length string. there's no difference with using [] and [number].
	//char uname, ups[5];
  
  //string class
	//string name_DB = "Homer"; //c-string doesn't recommend, '\0' means that the variable is string. if c-string variable doesn't contain '\0', it is not a string. it's array
	//string name;
	//string ps; // can save 5 length string.
	//string uname, ups;
	//while (true) {
	//	cout << "type new user name>";
	//	getline(cin, name); //save keyboard input. strings saved with arrangement form, example:name = {'h', 'o', '\0'}
	//	if (name != name_DB) {
	//		while (true) {
	//			cout << "set new user passward(passward must number, passward's length must less than 4)>";
	//			cin >> ps;
	//			cout << "new user name>" << name << endl << "new passward>" << ps << endl;
	//			if (true) {
	//				while (true) {
	//					cout << "type user name>";
	//					cin >> uname;
	//					if (uname == name) {
	//						cout << "type user passward>";
	//						cin >> ups;
	//						if (ups == ps) {
	//							cout << "welcome " << uname << "user" << endl;
	//							break;
	//						}
	//						else
	//							cout << "wrong passward" << endl;
	//					}
	//					else
	//						cout << "we don't have " << uname << " user" << endl;
	//				}
	//			}
	//		}
	//		break;
	//	}
	//	else
	//		cout << "we have same user name that you typed" << endl;
	//}
  
  
	/*practice question 77p:
  char city[21];
	cout << "type your city's name>";
	cin.getline(city, 21, '.');
	cout << "your city's name>" << city;*/
 return 0; //"return 0;" can omit.
}
