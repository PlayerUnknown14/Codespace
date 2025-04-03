#include<iostream>        
using namespace std;

struct Info
         {
                int d;
          };

struct Node
            {
                   Info info;
                   Node *next;
             };
Node * first (void);
Node * add (Node * pend);
void  print (Node * pbegin);
int main (void)
{
   Node *pbegin, *pend;
   int  i;
   pend=pbegin=first();  //создали список
   for(i=0; i<5; i++)               //добавили еще 5 элементов в список
             pend=add (pend);
    print(pbegin);   //вывели весь список на экран
     return 0;
}
//Начальное формирование списка
Node * first (void)
{
      //Выделяем память под элемент списка
     Node * pv=new Node;
    cout<<" \nВведите число: ";
     cin>>pv->info.d;
     pv->next=0;   //Адрес последней структуры в списке - 0
     return pv;   //возврат адреса начала списка
}
//Добавление элемента в конец списка
Node * add(Node * pend)
{
    //Выделяем память под очередной элемент списка
    Node * pv=new Node;
    cout<<"\nВведите число";
    cin>>pv->info.d;
     pv->next=0;   //Адрес последней структуры в списке - 0
     pend->next=pv;   //Сцепляем по адресу созданную структуру со списком
     return  pv; //возврат нового адреса последней структуры в списке
}
//Вывод списка на экран
int voidprint(Node * pbegin)
{
     Node * pv=pbegin;
     while (pv)   //пока адрес текущей структуры списка не 0
     {
          cout<<pv->info.d<<endl;
          pv=pv->next;   //переход к следующей структуре в списке
     }
    return 0;
}