#include <iostream>
#include "FruitUI.h"
frtui::FruitUI::FruitUI(FruitController *controller) {
    this->controller=controller;
}

std::string frtui::FruitUI::menu() {
    std::string menu_f="\n0. Exit\n1. Add fruit\n2. Delete fruit\n3. Search fruit by name\n4. See fruits by quantity\n5. See fruits sorted by expiration date\n6. See all  ";

    return menu_f ;
}

void frtui::FruitUI::read_attr(std::string& name, std::string& origin, std::string& expiration_date, int& price, int& quantity) {
    std::cout << "Enter the name of the fruit: ";
    std::cin >> name;
    std::cout<<std::endl;
    std::cout << "Enter the origin of the fruit: ";
    std::cin >> origin;
    std::cout<<std::endl;
    std::cout << "Enter the expiration date of the fruit(year,month,day): ";
    std::cin >> expiration_date;
    std::cout<<std::endl;
    std::cout << "Enter the price of the fruit: ";
    std::cin >> price;
    std::cout<<std::endl;
    std::cout << "Enter the quantity: ";
    std::cin >> quantity;
}
void frtui::FruitUI::execute() {
    std::string choice;
    do {
        std::cout << menu() << std::endl;
        std::cout << "Enter your choice:";
        std::cin >> choice;std::cout<<std::endl;

    if (choice == "1"){
        std::string name, origin, expiration_date;
        int price, quantity;
        read_attr(name,origin,expiration_date,price,quantity);
        this->controller->add(name, origin, price, quantity, expiration_date);
    } else if (choice == "2") {
        std::string name, origin;
        std::cout << "Enter the name of the fruit: ";
        std::cin >> name;
        std::cout<<std::endl;
        std::cout << "Enter the origin of the fruit: ";
        std::cin >> origin;
        std::cout<<std::endl;
        this->controller->delete_fruit(name, origin);
    } else if (choice == "3") {
        std::string searched_name;
        std::cout<<"Enter the name of the searched fruit:"<<std::endl;
        std::cin.ignore();
        std::getline(std::cin, searched_name);
        std::vector<frt::Fruit> searched_fruits;
        searched_fruits=this->controller->find(searched_name);
        print_elements(searched_fruits);
    } else if (choice == "4") {
        int given_low_quantity;
        std::cout<<"Give a limit quantity: "<<std::endl;
        std::cin>>given_low_quantity;
        std::vector<frt::Fruit> searched_fruits;
        searched_fruits=this->controller->find_quantity(given_low_quantity);
        print_elements(searched_fruits);
    } else if (choice == "5") {
        std::vector<frt::Fruit> searched_fruits;
        searched_fruits=this->controller->get_sorted_by_expiration_date();
        print_elements(searched_fruits);
    } else if (choice == "6") {
        this->controller->get_all();
    } else if (choice == "0") {
        std::cout << "Exiting..." << std::endl;
    } else {
        std::cout << "Invalid choice!" << std::endl;
    }
        } while (choice != "0");
    }

void frtui::FruitUI::print_elements(std::vector<frt::Fruit> print_fr) {
    for(int i=0; i<print_fr.size();i++) {
        std::cout<<print_fr[i];
        std::cout << "-----------------------------" << std::endl;
    }
}






