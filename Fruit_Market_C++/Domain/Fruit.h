#include <iostream>

#ifndef LAB4_FRUIT_H
#define LAB4_FRUIT_H

namespace frt {
    class Fruit {
    private:
        std::string _name;
        std::string _origin;
        int _price;
        int _quantity;
        std::string _expiration_date;

    public:
        Fruit(std::string name, std::string origin, int price, int quantity, std::string expiration_date);

        std::string get_name() const;

        std::string get_origin() const;

        int get_price() const;

        int get_quantity() const;

        std::string get_expiration_date() const;

        void set_price(int new_price);

        void set_quantity(int new_quantity);

        friend std::ostream& operator<<(std::ostream& os, const Fruit& fruit);
    };
}

#endif //LAB4_FRUIT_H
