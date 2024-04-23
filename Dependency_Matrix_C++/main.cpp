#include <iostream>
#include "DSM.h"
#include <cassert>

int main() {

    DSM dsm(8);

    // Setăm numele elementelor
    dsm.set_Element_Name(0, "Brain");
    dsm.set_Element_Name(1, "Heart");
    dsm.set_Element_Name(2, "Lungs");
    dsm.set_Element_Name(3, "Nervous System");
    dsm.set_Element_Name(4, "Muscular System");
    dsm.set_Element_Name(5, "Muscle");
    dsm.set_Element_Name(6, "Endocrine System");
    dsm.set_Element_Name(7, "Liver");


    // Adăugăm legături între elemente
    dsm.addLink("Brain","Heart", 1);
    dsm.addLink("Heart", "Lungs", 1);
    dsm.addLink("Brain", "Nervous System", 1);
    //dsm.addLink("Brain", "Hands", 13);
    dsm.addLink("Nervous System", "Endocrine System", 1);
    dsm.addLink("Nervous System", "Muscular System", 1);
    dsm.addLink("Brain", "Endocrine System", 1);
    dsm.addLink("Endocrine System", "Liver", 1);
    dsm.addLink("Muscular System", "Muscle", 1);

    // Afisam numele elementelor și numărul total de legături
    std::cout << "The components of the system: ";
    for (int i = 0; i < dsm.size(); ++i) {
        std::cout << dsm.get_Name(i) << "; ";
    }
    std::cout << std::endl;
    std::cout<<std::endl;

    dsm.printMatrix();
    std::cout<<std::endl;
    std::cout << "Total number of connections: " << dsm.countAllLinks() << std::endl;
    std::cout<<std::endl;
    // Verificăm dacă există o legătură între două elemente și afișăm greutatea legăturii
    std::string from ="Brain";
    std::string to = "Heart";
    if (dsm.hasLink(from, to)) {
        std::cout << "Between " << from << " and " << to << ", is a connection with weight: " << dsm.linkWeight(from, to) << std::endl;
    } else {
        std::cout << "There is no connection between " << from << " and " << to << std::endl;
    }
    std::cout<<std::endl;
    std::string name="Endocrine System";
    std::cout<<"To "<<name<<" there are " <<dsm.countToLinks(name)<<" connections"<<std::endl;
    std::cout<<std::endl;
    std::string name2="Brain";
    std::cout<<"From "<<name2<<" there are " <<dsm.countFromLinks(name2)<<" connections"<<std::endl;
    std::cout<<std::endl;
    std::cout<<"There are totally "<<dsm.countAllLinks()<<" connections"<<std::endl;
    std::cout<<"--------------------------------------------------------------------------------";
    std::string elementNames[] = {"Brain", "Heart", "Lungs","Nervous System","Muscular System","Muscle","Endocrine System","Liver"};
    int elementCount = sizeof(elementNames) / sizeof(elementNames[0]);
    DSM dsm2(elementNames, elementCount);
    dsm2.addLink("Brain","Heart", 1);
    dsm2.addLink("Heart", "Lungs", 1);
    dsm2.addLink("Brain", "Nervous System", 1);
    //dsm2.addLink("Brain", "Nervous System", 1);
    dsm2.addLink("Nervous System", "Endocrine System", 1);
    dsm2.addLink("Nervous System", "Muscular System", 1);
    dsm2.addLink("Brain", "Endocrine System", 1);
    dsm2.addLink("Endocrine System", "Liver", 1);
    dsm2.addLink("Muscular System", "Muscle", 1);
    std::cout<<std::endl;

    dsm2.printMatrix();
    std::cout<<"--------------------------------------------------------------------------------"<<std::endl;
    DSM dsm4=dsm;
    std::cout<<"Kopierkonstruktor size: "<<dsm4.size();
    DSM dsm3(3);

    // Setăm numele elementelor
    dsm3.set_Element_Name(0, "A");
    dsm3.set_Element_Name(1, "B");
    dsm3.set_Element_Name(2, "C");

    // Adăugăm legături între elemente
    dsm3.addLink("A", "B", 1);
    dsm3.addLink("B", "C", 1);
    dsm3.addLink("C", "A", 1);


    assert(dsm3.get_Name(0) == "A");
    assert(dsm3.get_Name(1) == "B");
    assert(dsm3.get_Name(2) == "C");
    assert(dsm3.countAllLinks() == 3);


    std::string from2 = "A";
    std::string to2 = "B";
    assert(dsm3.hasLink(from2, to2)==true);
    assert(dsm3.linkWeight(from2, to2) == 1);

    return 0;
}
