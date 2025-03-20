#include <iostream>


void fill_array(int* const arr, const int& size) {
    for (int i = 0; i < size; ++i) {
        arr[i] = rand() % 1001 - 500;
    }
}

void show_array(const int* const arr, const int size) {
    std::cout << "Elements of array:\t";

    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << '\t';
    }

    std::cout << '\n';
}

void push_back(int*& arr, int& size, int value) {
    int* newArr = new int[size + 1];

    for (int i = 0; i < size; ++i) {
        newArr[i] = arr[i];
    }

    delete[] arr;
    newArr[size++] = value;
    arr = newArr;
}

void pop_back(int*& arr, int& size) {
    if (!size) return;

    int* newArr = new int[--size];

    for (int i = 0; i < size; ++i) {
        newArr[i] = arr[i];
    }

    delete[] arr;
    arr = newArr;
}

void push_begin(int*& arr, int& size, int value) {
    int* newArr = new int[size + 1];

    newArr[0] = value;
    for (int i = 0; i < size; ++i) {
        newArr[i + 1] = arr[i];
    }

    delete[] arr;
    arr = newArr;
}

void pop_begin(int*& arr, int& size) {
    if (!size) return;

    int* newArr = new int[--size];

    for (int i = 0; i < size; ++i) {
        newArr[i] = arr[i + 1];
    }

    delete[] arr;
    arr = newArr;
}

int main() {
    srand(time(0));

    int const size = 5;
    int* arr = new int[size];

    fill_array(arr, size);
    show_array(arr, size);

    return 0;
}