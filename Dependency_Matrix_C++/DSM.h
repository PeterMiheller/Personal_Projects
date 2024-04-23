#ifndef LAB3_DSM_H
#define LAB3_DSM_H

#include <string>
#include "Vector.h"


class DSM {

private:
    int count;
    int **matrix;
    //std::vector<std::string> elementNames = std::vector<std::string>(0);
    Vector<std::string>* elementNames;


public:
    DSM(int elementCount);

    DSM(std::string elementNames[], int elementCount);

    DSM(const DSM& rhs);

    ~DSM();

public:
    int size();

    std::string get_Name(int index);

    void set_Element_Name(int index, std::string elementName);

    void addLink(std::string fromElement, std::string toElement, int weight);

    void deleteLink(std::string fromElement, std::string toElement);

    bool hasLink(std::string fromElement, std::string toElement);

    int linkWeight(std::string fromElement, std::string toElement);

    int countToLinks(std::string elementName);

    int countFromLinks(std::string elementName);

    int countAllLinks();

    void printMatrix();

    void resize();

};


#endif //LAB3_DSM_H
