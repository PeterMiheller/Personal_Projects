#include <algorithm>
#include "FruitRepo.h"


void frtrepository::FruitRepo::delete_fruit(const std::string &name, const std::string &origin) {
    bool found = false;
    for (int i = 0; i < this->fruit_repo.size(); i++) {
        if (this->fruit_repo[i].get_name() == name && this->fruit_repo[i].get_origin() == origin) {
            found = true;
            this->fruit_repo.erase(this->fruit_repo.begin() + i);
            std::cout << "Fruit deleted successfully"<<std::endl;
            break;
        }
    }
    if (!found) {
        std::cout << "Fruit does not exist"<<std::endl;
    }
}

void frtrepository::FruitRepo::add(const Fruit &fruit) {
    bool found = false;
    for (int i = 0; i < this->fruit_repo.size(); i++) {
        if (this->fruit_repo[i].get_name() == fruit.get_name() &&
            this->fruit_repo[i].get_origin() == fruit.get_origin()) {
            this->fruit_repo[i].set_quantity(this->fruit_repo[i].get_quantity() + fruit.get_quantity());
            found = true;
        }
    }
    if (!found) {
        this->fruit_repo.push_back(fruit);
        std::cout << "Fruit added successfully"<<std::endl;
    }

}

void frtrepository::FruitRepo::get_all() const {
    if (this->fruit_repo.empty()) {
        std::cout << "No fruits" << std::endl;
    } else {
        std::vector<Fruit> sorted_fruits = this->fruit_repo;
        std::sort(sorted_fruits.begin(), sorted_fruits.end(),
                  [](const Fruit &a, const Fruit &b) {
                      return a.get_name() < b.get_name();
                  });
        for (const Fruit &fruit: sorted_fruits) {
            std::cout << "Name: " << fruit.get_name() << std::endl;
            std::cout << "Origin: " << fruit.get_origin() << std::endl;
            std::cout << "Price: " << fruit.get_price() << std::endl;
            std::cout << "Quantity: " << fruit.get_quantity() << std::endl;
            std::cout << "Expiration Date: " << fruit.get_expiration_date() << std::endl;
            std::cout << "-----------------------------" << std::endl;
        }
    }
}

std::vector<Fruit> frtrepository::FruitRepo::find(std::string name) const {
    std::vector<Fruit> found_fruits;
    if (name.empty()) {
        found_fruits = this->fruit_repo;
        std::sort(found_fruits.begin(), found_fruits.end(),
                  [](const Fruit &a, const Fruit &b) {
                      return a.get_name() < b.get_name();
                  });
        return found_fruits;
    }
    bool found = false;
    for (const Fruit &fruit: this->fruit_repo) {
        if (fruit.get_name().find(name) != -1) {
            found_fruits.push_back(fruit);
            found = true;
        }
    }
    if (!found) {
        std::cout << "No fruits found with the given name." << std::endl;
    }
    return found_fruits;
}

std::vector<Fruit> frtrepository::FruitRepo::find_quantity(int quantity) const {
    std::vector<Fruit> found_fruits;
    for (const Fruit &fruit: this->fruit_repo) {
        if (fruit.get_quantity() <= quantity) {
            found_fruits.push_back(fruit);
        }
    }
    return found_fruits;
}

std::vector<Fruit> frtrepository::FruitRepo::get_sorted_by_expiration_date() const {
    if (this->fruit_repo.empty()) {
        std::cout << "No fruits" << std::endl;
    }
    std::vector<Fruit> sorted_fruits = this->fruit_repo;
    std::sort(sorted_fruits.begin(), sorted_fruits.end(),
              [](const Fruit &a, const Fruit &b) {
                  return a.get_expiration_date() < b.get_expiration_date();
              });
    return sorted_fruits;
}

