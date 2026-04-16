using System;
using System.Collections;
using System.Collections.Generic;

namespace Lab4
{
    // Класс Time теперь реализует IComparable для сортировки "по умолчанию"
    class Time : IComparable<Time>
    {
        private int _hours;
        private int _minutes;
        private int _seconds;

        public int Hours
        {
            get => _hours;
            set { if (value < 0 || value > 23) throw new ArgumentException(); _hours = value; }
        }

        public int Minutes
        {
            get => _minutes;
            set { if (value < 0 || value > 59) throw new ArgumentException(); _minutes = value; }
        }

        public int Seconds
        {
            get => _seconds;
            set { if (value < 0 || value > 59) throw new ArgumentException(); _seconds = value; }
        }

        public Time(int h, int m, int s)
        {
            Hours = h; Minutes = m; Seconds = s;
        }

        // Метод для получения общего количества секунд (для удобства сравнения)
        public int ToTotalSeconds() => _hours * 3600 + _minutes * 60 + _seconds;

        // Реализация IComparable: Сортировка по возрастанию времени
        public int CompareTo(Time other)
        {
            if (other == null) return 1;
            return this.ToTotalSeconds().CompareTo(other.ToTotalSeconds());
        }

        public override string ToString() => $"{Hours:D2}:{Minutes:D2}:{Seconds:D2}";
    }

    // Вспомогательный класс для сортировки ТОЛЬКО по секундам (IComparer)
    class SecondsComparer : IComparer<Time>
    {
        public int Compare(Time x, Time y)
        {
            return x.Seconds.CompareTo(y.Seconds);
        }
    }

    // Вспомогательный класс для сортировки ТОЛЬКО по часам (IComparer)
    class HoursComparer : IComparer<Time>
    {
        public int Compare(Time x, Time y)
        {
            return x.Hours.CompareTo(y.Hours);
        }
    }

    class Program
    {
        static void Main()
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;

            // Создаем массив объектов времени
            Time[] times = new Time[]
            {
                new Time(15, 30, 10),
                new Time(10, 10, 50),
                new Time(23, 00, 05),
                new Time(05, 45, 30)
            };

            Console.WriteLine("Исходный список:");
            PrintArray(times);

            // 1. Сортировка по умолчанию (использует IComparable - хронологически)
            Array.Sort(times);
            Console.WriteLine("\nСортировка по умолчанию (хронологическая):");
            PrintArray(times);

            // 2. Сортировка через IComparer (по секундам)
            Array.Sort(times, new SecondsComparer());
            Console.WriteLine("\nСортировка по секундам (используя IComparer):");
            PrintArray(times);

            // 3. Сортировка через IComparer (по часам)
            Array.Sort(times, new HoursComparer());
            Console.WriteLine("\nСортировка по часам (используя IComparer):");
            PrintArray(times);

            Console.ReadKey();
        }

        static void PrintArray(Time[] array)
        {
            foreach (var t in array) Console.WriteLine(t);
        }
    }
}