#include "../Domain/Fruit.h"
#include <iostream>
#include <vector>
using namespace frt;

#ifndef LAB4_FRUITREPO_H
#define LAB4_FRUITREPO_H

namespace frtrepository {
    class FruitRepo {
    private:
        std::vector<Fruit> fruit_repo;
    public:
        void add(const Fruit& fruit);

        void delete_fruit(const std::string& name,const std::string& origin);

        void get_all() const;

        std::vector<Fruit> find(std::string name) const;

        std::vector<Fruit> find_quantity(int quantity) const;

        std::vector<Fruit> get_sorted_by_expiration_date() const;
    };
}

#endif //LAB4_FRUITREPO_H
