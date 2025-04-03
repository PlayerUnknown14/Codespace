#include <iostream>
using namespace std;

struct Info {
    int d;
};

struct Node {
    Info info;
    Node* next;
    Node* prev;  // Добавляем указатель на предыдущий элемент
};

// Прототипы функций
Node* first(void);
Node* add(Node* pend);
void printForward(Node* pbegin);
void printBackward(Node* pend);

int main(void) {
    Node *pbegin, *pend;
    int i;
    
    // Создаем первый элемент списка
    pend = pbegin = first();
    
    // Добавляем еще 5 элементов в список
    for(i = 0; i < 5; i++) {
        pend = add(pend);
    }
    
    // Выводим список от начала к концу
    cout << "\nСписок сверху вниз (от начала к концу):\n";
    printForward(pbegin);
    
    // Выводим список от конца к началу
    cout << "\nСписок снизу вверх (от конца к началу):\n";
    printBackward(pend);
    
    return 0;
}

// Начальное формирование списка
Node* first(void) {
    Node* pv = new Node;
    cout << "Введите число: ";
    cin >> pv->info.d;
    pv->next = nullptr;  // nullptr вместо 0 для современного C++
    pv->prev = nullptr;  // У первого элемента нет предыдущего
    return pv;
}

// Добавление элемента в конец списка
Node* add(Node* pend) {
    Node* pv = new Node;
    cout << "Введите число: ";
    cin >> pv->info.d;
    pv->next = nullptr;   // Новый элемент будет последним
    pv->prev = pend;      // Связываем новый элемент с предыдущим
    pend->next = pv;      // Связываем предыдущий элемент с новым
    return pv;            // Возвращаем новый конец списка
}

// Вывод списка от начала к концу
void printForward(Node* pbegin) {
    Node* pv = pbegin;
    while (pv) {
        cout << pv->info.d << " ";
        pv = pv->next;
    }
    cout << endl;
}

// Вывод списка от конца к началу
void printBackward(Node* pend) {
    Node* pv = pend;
    while (pv) {
        cout << pv->info.d << " ";
        pv = pv->prev;
    }
    cout << endl;
}