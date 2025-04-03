#include <iostream>
using namespace std;

struct Student {
    string fullName;
    string groupNumber;
    string addressType;
};

struct Node {
    Student student;
    Node* next;
    Node* prev; 
};

Node* first(void);
Node* add(Node* pend);
void printForward(Node* pbegin, int size);
void printBackward(Node* pend, int size);

int main(void) {
    Node *pbegin, *pend;

    int studentNum;
    cout << "\nВведите количество студентов: ";
    cin >> studentNum;

    pend = pbegin = first();


    for(int i = 0; i < studentNum - 1; i++) {
        pend = add(pend);
    }

    cout << "\nСписок сверху вниз (от начала к концу):\n";
    printForward(pbegin, studentNum);
    
    cout << "\nСписок снизу вверх (от конца к началу):\n";
    printBackward(pend, studentNum);
    
    return 0;
}

Node* first(void) {
    Node* pv = new Node;
    cout << "Введите фамилию, имя и отчество студента: ";
    getline(cin >> ws, pv->student.fullName);
    cout << "Введите номер группы (например, БИ13-01): ";
    getline(cin, pv->student.groupNumber);
    cout << "Укажите место жительства (Parents/Dorms/Rent apparts): ";
    getline(cin, pv->student.addressType);
    pv->next = nullptr; 
    pv->prev = nullptr; 
    return pv;
}

Node* add(Node* pend) {
    Node* pv = new Node;
    cout << "Введите фамилию, имя и отчество студента: ";
    getline(cin >> ws, pv->student.fullName);
    cout << "Введите номер группы (например, БИ13-01): ";
    getline(cin, pv->student.groupNumber);
    cout << "Укажите место жительства (Parents/Dorms/Rent apparts): ";
    getline(cin, pv->student.addressType);
    pv->next = nullptr;  
    pv->prev = pend;     
    pend->next = pv;     
    return pv;           
}

void printForward(Node* pbegin, int size) {
    Node* pv = pbegin;
    while (pv) {
        for (int i = 0; i < size; ++i) {
            cout << "Данные студента №" << i + 1 << ": ";
            cout << "ФИО студента: " << pv->student.fullName << "; ";
            cout << "Группа: " << pv->student.groupNumber << "; ";
            cout << "Место проживания: " << pv->student.addressType << "; ";
            cout << endl;
            pv = pv->next;
        }
    }
}

void printBackward(Node* pend, int size) {
    Node* pv = pend;
    while (pv) {
        for (int i = size; i > 0; --i) {
            cout << "Данные студента №" << i << ": ";
            cout << "ФИО студента: " << pv->student.fullName << "; ";
            cout << "Группа: " << pv->student.groupNumber << "; ";
            cout << "Место проживания: " << pv->student.addressType << "; ";
            cout << endl;
            pv = pv->prev;
        }
    }
}