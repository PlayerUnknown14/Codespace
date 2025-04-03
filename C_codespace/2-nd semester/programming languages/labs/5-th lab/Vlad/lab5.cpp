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
void printForward(Node* pbegin);
void printBackward(Node* pend);

int main(void) {
    Node *pbegin, *pend;

    pend = pbegin = first();

    int i;
    for(i = 0; i < 1; i++) {
        pend = add(pend);
    }

    cout << "\nСписок сверху вниз (от начала к концу):\n";
    printForward(pbegin);
    
    cout << "\nСписок снизу вверх (от конца к началу):\n";
    printBackward(pend);
    
    return 0;
}

Node* first(void) {
    Node* pv = new Node;
    cout << "Введите фамилию, имя и отчество студента: ";
    cin >> pv->student.fullName;
    cout << "Введите номер группы (например, БИ13-01): ";
    cin >> pv->student.groupNumber;
    cout << "Укажите место жительства (Parents/Dorms/Rent apparts): ";
    cin >> pv->student.addressType;
    pv->next = nullptr; 
    pv->prev = nullptr; 
    return pv;
}

Node* add(Node* pend) {
    Node* pv = new Node;
    cout << "Введите фамилию, имя и отчество студента: ";
    cin >> pv->student.fullName;
    cout << "Введите номер группы (например, БИ13-01): ";
    cin >> pv->student.groupNumber;
    cout << "Укажите место жительства (Parents/Dorms/Rent apparts): ";
    cin >> pv->student.addressType;
    pv->next = nullptr;  
    pv->prev = pend;     
    pend->next = pv;     
    return pv;           
}

void printForward(Node* pbegin) {
    Node* pv = pbegin;
    while (pv) {
        cout << "ФИО студента: " << pv->student.fullName << "; ";
        cout << "Группа: " << pv->student.groupNumber << "; ";
        cout << "Место проживания: " << pv->student.addressType << "; ";
        cout << endl;
        pv = pv->next;
    }
    cout << endl;
}

void printBackward(Node* pend) {
    Node* pv = pend;
    while (pv) {
        cout << "ФИО студента: " << pv->student.fullName << "; ";
        cout << "Группа: " << pv->student.groupNumber << "; ";
        cout << "Место проживания: " << pv->student.addressType << "; ";
        cout << endl;
        pv = pv->prev;
    }
    cout << endl;
}