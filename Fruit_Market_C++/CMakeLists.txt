cmake_minimum_required(VERSION 3.27)
project(Lab4)

set(CMAKE_CXX_STANDARD 17)

add_executable(Lab4
        UI/FruitUI.h
        Controller/FruitController.h
        Repo/FruitRepo.h
        Domain/Fruit.h
        Controller/FruitController.cpp
        Repo/FruitRepo.cpp
        Domain/Fruit.cpp
        UI/FruitUI.cpp
        FruitApp.cpp)
