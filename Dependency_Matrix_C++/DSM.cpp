#include <iostream>
#include <string>
#include "DSM.h"

DSM::DSM(int elementCount) {
    this->count = elementCount;
    this->elementNames = new Vector<std::string>(this->count);

    // Inițializarea matricei cu dimensiunea corespunzătoare
    this->matrix = new int *[this->count];
    for (int i = 0; i < this->count; i++) {
        this->matrix[i] = new int[this->count];
    }
    // Inițializarea matricei cu  zero
    for (int i = 0; i < this->count; i++) {
        for (int j = 0; j < this->count; j++) {
            this->matrix[i][j] = 0;
        }
    }



    //elementNames = std::vector<std::string>(this->count);
    for (int i = 0; i < this->count; i++) {
        //elementNames.push_back("");
        this->elementNames->add("");
    }


}

DSM::DSM(const DSM &rhs) {

    // Copiem toate componentele prin rhs care este o referinta catre un obiect DSM
    this->count = rhs.count;


    this->matrix = new int *[this->count];
    for (int i = 0; i < this->count; i++) {
        this->matrix[i] = new int[this->count];
    }


    for (int i = 0; i < this->count; i++) {
        for (int j = 0; j < this->count; j++) {
            this->matrix[i][j] = rhs.matrix[i][j];
        }
    }


    this->elementNames = new Vector<std::string>(this->count);
    for (size_t i = 0; i < this->count; ++i) {
        this->elementNames->add(rhs.elementNames->current(i));
    }

}


DSM::DSM(std::string elementNames[], int elementCount) {
    this->count = elementCount;
    this->elementNames = new Vector<std::string>(this->count);

    this->matrix = new int *[this->count];
    for (int i = 0; i < this->count; i++) {
        this->matrix[i] = new int[this->count];
    }
    for (int i = 0; i < this->count; i++) {
        for (int j = 0; j < this->count; j++) {
            this->matrix[i][j] = 0;
        }
    }

    for (int i = 0; i < this->count; i++) {
        //this->elementNames.push_back(elementNames[i]);
        this->elementNames->add(elementNames[i]);
    }


}

DSM::~DSM() {
    for (int i = 0; i < this->count; i++) {
        delete[] this->matrix[i];
    }
    delete[] this->matrix;
    delete this->elementNames;
}

int DSM::size() {
    return this->count;
}

std::string DSM::get_Name(int index) {
//   return elementNames[index];
    return this->elementNames->current(index);


}

//elementNames este un pointer la obiectul Vector<std::string>, iar * dereferentiaza pointerul la obiectul Vector
// deoarece operatorul [] este supraincarcat pentru a permite accesul la elementele vectorului prin indexare.
void DSM::set_Element_Name(int index, std::string elementName) {
    //elementNames[index] = elementName;
    //elementNames->current(index)=elementName;
    (*elementNames)[index] = elementName;


}

void DSM::addLink(std::string fromElement, std::string toElement, int weight) {
    int fromIndex = -1;
    for (int i = 0; i < this->count; ++i) {
        if (this->elementNames->current(i) == fromElement) {
            fromIndex = i;
            break;
        }
    }

    int toIndex = -1;
    for (int i = 0; i < this->count; ++i) {
        if (this->elementNames->current(i) == toElement) {
            toIndex = i;
            break;
        }
    }

// daca gasim ambele elemente
    if (fromIndex != -1 && toIndex != -1) {
        this->matrix[fromIndex][toIndex] = weight;
    }//daca nu gasim un element adaugam in vector si redimensionam matricea
    else if (fromIndex == -1) {
        this->elementNames->add(fromElement);
        resize();
        this->matrix[this->count - 1][toIndex] = weight;//this->count-1 pentru ca e ultimul element adaugat
    } else if (toIndex == -1) {
        this->elementNames->add(toElement);
        resize();
        this->matrix[fromIndex][this->count - 1] = weight;
    }
}

void DSM::deleteLink(std::string fromElement, std::string toElement) {
    int fromIndex = -1;
    for (int i = 0; i < this->count; ++i) {
        if (this->elementNames->current(i) == fromElement) {
            fromIndex = i;
            break;
        }
    }


    int toIndex = -1;
    for (int i = 0; i < this->count; ++i) {
        if (this->elementNames->current(i) == toElement) {
            toIndex = i;
            break;
        }
    }


    if (fromIndex != -1 && toIndex != -1) {
        this->matrix[fromIndex][toIndex] = 0;
    } else {

        std::cout << "Error" << std::endl;
    }
}

bool DSM::hasLink(std::string fromElement, std::string toElement) {
    int fromIndex = -1;
    for (int i = 0; i < this->count; ++i) {
        if (this->elementNames->current(i) == fromElement) {
            fromIndex = i;
            break;
        }
    }


    int toIndex = -1;
    for (int i = 0; i < this->count; ++i) {
        if (this->elementNames->current(i) == toElement) {
            toIndex = i;
            break;
        }
    }


    if (fromIndex != -1 && toIndex != -1 && this->matrix[fromIndex][toIndex] != 0) {
        return true;
    } else {
        return false;
    }
}

int DSM::linkWeight(std::string fromElement, std::string toElement) {
    int fromIndex = -1;
    for (int i = 0; i < this->count; ++i) {
        if (this->elementNames->current(i) == fromElement) {
            fromIndex = i;
            break;
        }
    }


    int toIndex = -1;
    for (int i = 0; i < this->count; ++i) {
        if (this->elementNames->current(i) == toElement) {
            toIndex = i;
            break;
        }
    }


    if (fromIndex != -1 && toIndex != -1 && this->matrix[fromIndex][toIndex] != 0) {
        return this->matrix[fromIndex][toIndex];
    } else {
        std::cout << "No connection between them";
    }
}

int DSM::countFromLinks(std::string elementName) {
    int index = -1;
    for (int i = 0; i < this->count; ++i) {
        if (this->elementNames->current(i) == elementName) {
            index = i;
            break;
        }
    }


    if (index != -1) {
        int countFrom = 0;

        for (int i = 0; i < this->count; ++i) {

            if (this->matrix[index][i] != 0) {
                countFrom++;
            }
        }
        return countFrom;
    } else {

        return -1;
    }
}


int DSM::countToLinks(std::string elementName) {
    int index = -1;
    for (int i = 0; i < this->count; ++i) {
        if (this->elementNames->current(i) == elementName) {
            index = i;
            break;
        }
    }


    if (index != -1) {
        int countTo = 0;

        for (int i = 0; i < this->count; ++i) {

            if (this->matrix[i][index] != 0) {
                countTo++;
            }
        }
        return countTo;
    } else {

        std::cout << "There is no connection";
    }
}

int DSM::countAllLinks() {
    int totalLinks = 0;


    for (int i = 0; i < this->count; ++i) {
        for (int j = 0; j < this->count; ++j) {

            if (this->matrix[i][j] != 0) {
                totalLinks++;
            }
        }
    }

    return totalLinks;
}

void DSM::printMatrix() {

    for (int i = 0; i < this->count; i++) {
        for (int j = 0; j < this->count; j++) {
            std::cout << this->matrix[i][j] << " ";
        }
        std::cout << "\n";
    }
}

void DSM::resize() {
    int newCount = this->count + 1;
    int **newMatrix = new int *[newCount];
    for (int i = 0; i < newCount; i++) {
        newMatrix[i] = new int[newCount];
    }

    for (int i = 0; i < newCount; i++) {
        for (int j = 0; j < newCount; j++) {
            newMatrix[i][j] = 0;
        }
    }

    for (int i = 0; i < this->count; i++) {
        for (int j = 0; j < this->count; j++) {
            newMatrix[i][j] = this->matrix[i][j];
        }
    }


    for (int i = 0; i < this->count; i++) {
        delete[] this->matrix[i];
    }
    delete[] this->matrix;


    this->matrix = newMatrix;


    this->count = newCount;
}



