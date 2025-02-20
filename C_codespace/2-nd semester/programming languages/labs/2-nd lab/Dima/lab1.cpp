// Вариант 13
// Объект для разработки структуры – самолет. 
// Объявить поля:
// –	Фамилия, имя отчество  пассажира
// –	Тип самолета
// –	Номер рейса
// –	Пункт назначения
// –	Время отправления (структура с полями часы, минуты)

#include <iostream>
#include <string>

using namespace std;

struct Time {
    int hours;
    int minutes;
};

struct Passenger {
    string lastName;
    string firstName;
    string middleName;
};

struct Flight {
    Passenger passenger;
    string airplaneType;
    string flightNumber;
    string destination;
    Time departureTime;
};

// Функция для ввода данных о рейсе
void inputFlight(Flight &flight) {
    cout << "Введите фамилию пассажира: ";
    getline(cin, flight.passenger.lastName);
    
    cout << "Введите имя пассажира: ";
    getline(cin, flight.passenger.firstName);
    
    cout << "Введите отчество пассажира: ";
    getline(cin, flight.passenger.middleName);
    
    cout << "Введите тип самолета: ";
    getline(cin, flight.airplaneType);
    
    cout << "Введите номер рейса: ";
    getline(cin, flight.flightNumber);
    
    cout << "Введите пункт назначения: ";
    getline(cin, flight.destination);
    
    cout << "Введите время отправления (часы): ";
    cin >> flight.departureTime.hours;
    
    cout << "Введите время отправления (минуты): ";
    cin >> flight.departureTime.minutes;

    // Очистка буфера ввода после cin
    cin.ignore();
}

// Функция для вывода данных о рейсе
void outputFlight(const Flight &flight) {
    cout << "Пассажир: " << flight.passenger.lastName << " "
              << flight.passenger.firstName << " "
              << flight.passenger.middleName << endl;
    cout << "Тип самолета: " << flight.airplaneType << endl;
    cout << "Номер рейса: " << flight.flightNumber << endl;
    cout << "Пункт назначения: " << flight.destination << endl;
    cout << "Время отправления: " 
              << flight.departureTime.hours << ":" 
              << (flight.departureTime.minutes < 10 ? "0" : "") 
              << flight.departureTime.minutes << endl;
}

int main() {
    const int MAX_FLIGHTS = 3;
    Flight flights[MAX_FLIGHTS];

    for (int i = 0; i < MAX_FLIGHTS; ++i) {
        std::cout << "\nВведите данные для рейса #" << (i + 1) << ":\n";
        inputFlight(flights[i]);
    }

    cout << "\nДанные о рейсах:\n";
    for (int i = 0; i < MAX_FLIGHTS; ++i) {
        cout << "\nРейс #" << (i + 1) << ":\n";
        outputFlight(flights[i]);
    }

    return 0;
}
