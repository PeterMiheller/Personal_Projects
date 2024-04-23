#include <iostream>


template <typename T>
class Vector
{
private:
    size_t _size = 0;
    size_t _capacity = 0;
    T* _elements = nullptr;

private:
    void _resize();

public:
    Vector(size_t cap);
    ~Vector();

    void add(T i);
    void print();
    T current(size_t index);
    T& operator[](size_t index);
};


template<typename T>
Vector<T>::Vector(size_t cap)
{
    this->_capacity = cap;
    this->_elements = new T[cap];
}

template<typename T>
Vector<T>::~Vector()
{
    delete[] this->_elements;
}

template<typename T>
void Vector<T>::_resize()
{
    _capacity = 2 * _size;
    T* tmp = new T[_capacity];

    for (size_t i = 0; i < _size; i++)
    {
        tmp[i] = _elements[i];
    }

    delete[] _elements;
    _elements = tmp;
}

template<typename T>
void Vector<T>::add(T i)
{
    if (_capacity == 0)
    {
        _resize();
        // *((unsigned int*)0) = 0xDEAD;
    }

    _capacity--;
    _elements[_size] = i;
    _size++;
}

template<typename T>
void Vector<T>::print()
{
    for (size_t i = 0; i < _size; i++)
    {
        std::printf("%d ", _elements[i]);
    }

    std::printf("\n");
}
//facem o copie a elementului pentru comparari
template<typename T>
T Vector<T>::current(size_t index)
{
    if ( index < _size)
    {
        return _elements[index];
    }
}
//referinta la obiect pentru schimbarea valorii
template<typename T>
T& Vector<T>::operator[](size_t index) {
    if (index >= _size) {
        throw std::out_of_range("Index out of range");
    }
    return _elements[index];
}