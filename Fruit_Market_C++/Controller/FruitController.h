#include <iostream>
#ifndef LAB4_FRUITCONTROLLER_H
#define LAB4_FRUITCONTROLLER_H
#include "../Repo/FruitRepo.h"
using namespace frtrepository;
namespace ftrcontroller {
    class FruitController {
    public:
        FruitController(FruitRepo *repo);

        void add(std::string name, std::string origin, int price, int quantity, std::string expiration_date);

        void delete_fruit(const std::string& name, const std::string& origin);

        std::vector<Fruit> find(std::string name) const;

        std::vector<Fruit> find_quantity(int quantity) const;

        std::vector<Fruit> get_sorted_by_expiration_date() const;

        void get_all() const;

    private:
        FruitRepo *repo = nullptr;
        //std::vector<Fruit> _fruit_list;
    };

}
#endif //LAB4_FRUITCONTROLLER_H
