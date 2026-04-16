using System;

namespace Lab3
{
    // Базовый класс
    abstract class Engine
    {
        public string Model { get; set; }
        public int Power { get; set; }

        public Engine(string model, int power)
        {
            Model = model;
            Power = power;
        }

        // Виртуальный метод для вывода (полиморфизм)
        public virtual void Print()
        {
            Console.WriteLine($"Двигатель: {Model}, Мощность: {Power}");
        }

        // Сравнение объектов по значениям 
        public override bool Equals(object obj)
        {
            if (obj == null || GetType() != obj.GetType()) return false;
            Engine other = (Engine)obj;
            return Model == other.Model && Power == other.Power;
        }

        public override int GetHashCode() => (Model, Power).GetHashCode();
    }

    // ДВС
    class Ice : Engine
    {
        public int Cyls { get; set; } // Кол-во цилиндров

        public Ice(string model, int power, int cyls) : base(model, power)
        {
            Cyls = cyls;
        }

        public override void Print()
        {
            Console.WriteLine($"ДВС: {Model}, Мощность: {Power}, Цилиндров: {Cyls}");
        }

        public override bool Equals(object obj)
        {
            if (!base.Equals(obj)) return false;
            return Cyls == ((Ice)obj).Cyls;
        }
    }

    // Дизель (наследует ДВС)
    class Diesel : Ice
    {
        public double Fuel { get; set; } // Расход топлива

        public Diesel(string model, int power, int cyls, double fuel) : base(model, power, cyls)
        {
            Fuel = fuel;
        }

        public override void Print()
        {
            Console.WriteLine($"Дизель: {Model}, Мощность: {Power}, Расход: {Fuel}л");
        }

        public override bool Equals(object obj)
        {
            if (!base.Equals(obj)) return false;
            return Fuel == ((Diesel)obj).Fuel;
        }
    }

    // Реактивный двигатель
    class Jet : Engine
    {
        public int Thrust { get; set; } // Тяга

        public Jet(string model, int power, int thrust) : base(model, power)
        {
            Thrust = thrust;
        }

        public override void Print()
        {
            Console.WriteLine($"Реактивный: {Model}, Мощность: {Power}, Тяга: {Thrust}кН");
        }

        public override bool Equals(object obj)
        {
            if (!base.Equals(obj)) return false;
            return Thrust == ((Jet)obj).Thrust;
        }
    }

    class Program
    {
        static void Main()
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Engine[] list = new Engine[3];

            list[0] = new Ice("V8", 400, 8);
            list[1] = new Diesel("D-100", 250, 4, 12.5);
            list[2] = new Jet("Turbo-X", 10000, 80);

            Console.WriteLine("Список двигателей:");
            foreach (var e in list)
            {
                e.Print();
            }

            // Проверка Equals
            Diesel d1 = new Diesel("Test", 100, 4, 10);
            Diesel d2 = new Diesel("Test", 100, 4, 10);
            Console.WriteLine("\nОбъекты d1 и d2 равны: " + d1.Equals(d2));

            Console.ReadKey();
        }
    }
}