#include "../Controller/FruitController.h"
#include <memory>
#ifndef LAB4_FRUITUI_H
#define LAB4_FRUITUI_H
using namespace ftrcontroller;
namespace frtui {
    class FruitUI {
    public:
        FruitUI(FruitController *controller);

        std::string menu();

        void execute();

        void read_attr(std::string &name, std::string &origin, std::string &expiration_date, int &price, int &quantity);

        void print_elements(std::vector<frt::Fruit>);

    private:
        FruitController *controller= nullptr;
    };
}

#endif //LAB4_FRUITUI_H
