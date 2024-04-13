#include <memory>
#include "Repo/FruitRepo.h"
#include "Controller/FruitController.h"
#include "UI/FruitUI.h"
using namespace frtui;
using namespace ftrcontroller;
using namespace frtrepository;
int main()
{
    std::unique_ptr<frtrepository::FruitRepo> repository = std::make_unique<frtrepository::FruitRepo>();
    std::unique_ptr<ftrcontroller::FruitController> controller = std::make_unique<ftrcontroller::FruitController>(repository.get());
    std::unique_ptr<frtui::FruitUI> ui = std::make_unique<frtui::FruitUI>(controller.get());
    ui->execute();
    return 0;
}