#include "FruitController.h"
ftrcontroller::FruitController::FruitController(frtrepository::FruitRepo *repo)  {
    this->repo=repo;
}

void ftrcontroller::FruitController::add(std::string name, std::string origin, int price, int quantity, std::string expiration_date) {
    auto add_fruit=Fruit(name,origin,price,quantity,expiration_date);
    this->repo->add(add_fruit);
}

void ftrcontroller::FruitController::delete_fruit(const std::string& name, const std::string& origin) {
    this->repo->delete_fruit(name,origin);
}

std::vector<Fruit> ftrcontroller::FruitController::find(std::string name) const {
    return this->repo->find(name);
}

std::vector<Fruit> ftrcontroller::FruitController::find_quantity(int quantity) const {
    return this->repo->find_quantity(quantity);
}

std::vector<Fruit> ftrcontroller::FruitController::get_sorted_by_expiration_date() const {
    return this->repo->get_sorted_by_expiration_date();
}

void ftrcontroller::FruitController::get_all() const {
    this->repo->get_all();
}
