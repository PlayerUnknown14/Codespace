   #include <iostream>
   #include <fstream>
   #include <string>
   #include <locale>
   #include <codecvt>

   int main() {
       // Открываем файл в бинарном режиме
       std::wifstream file("test.txt", std::ios::binary);
       
       // Устанавливаем кодировку UTF-8
       file.imbue(std::locale(file.getloc(), new std::codecvt_utf8<wchar_t>));

       if (!file) {
           std::wcerr << "Ошибка при открытии файла!" << std::endl;
           return 1;
       }

       std::wstring line;
       while (std::getline(file, line)) {
           std::wcout << line << std::endl; // Выводим содержимое файла
       }

       file.close();
       return 0;
   }