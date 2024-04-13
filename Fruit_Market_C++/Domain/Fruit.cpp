
#include "Fruit.h"
frt::Fruit::Fruit(std::string name, std::string origin, int price, int quantity, std::string expiration_date) {
    this->_name=name;
    this->_origin=origin;
    this->_price=price;
    this->_quantity=quantity;
    this->_expiration_date=expiration_date;
}

std::string frt::Fruit::get_name() const {
    return this->_name;
}

std::string frt::Fruit::get_origin() const{
    return this->_origin;
}

int frt::Fruit::get_price() const {
    return this->_price;
}

void frt::Fruit::set_price(int new_price) {
    this->_price=new_price;
}

void frt::Fruit::set_quantity(int new_quantity) {
    this->_quantity=new_quantity;
}

int frt::Fruit::get_quantity() const {
   return this->_quantity;
}

std::string frt::Fruit::get_expiration_date() const {
    return this->_expiration_date;
}
std::ostream& frt::operator<<(std::ostream& os, const Fruit& fruit) {
    os << "Name: " << fruit.get_name() << std::endl;
    os << "Origin: " << fruit.get_origin() << std::endl;
    os << "Price: " << fruit.get_price() << std::endl;
    os << "Quantity: " << fruit.get_quantity() << std::endl;
    os << "Expiration Date: " << fruit.get_expiration_date() << std::endl;
    return os;
}