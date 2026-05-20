using System;
using System.Threading;
using System.Windows.Forms;
using System.Drawing;

namespace Lab9_Var12
{
    public class Form1 : Form
    {
        private Button btnCalculate = new Button { Text = "Вычислить ПИ", Location = new Point(20, 20), Width = 150 };
        private Label lblResult = new Label { Location = new Point(20, 60), Width = 300, Text = "Результат: ожидает вычисления..." };
        private ProgressBar progressBar = new ProgressBar { Location = new Point(20, 100), Width = 300, Minimum = 0, Maximum = 100 };

        public Form1()
        {
            Text = "Вычисление ПИ (Вар. 12)";
            Width = 400; Height = 200;
            Controls.AddRange(new Control[] { btnCalculate, lblResult, progressBar });

            btnCalculate.Click += (s, e) =>
            {
                btnCalculate.Enabled = false;
                // Создаем поток для фоновых вычислений
                Thread thread = new Thread(CalculatePi);
                thread.IsBackground = true; // Делаем поток фоновым
                thread.Start();
            };
        }

        private void CalculatePi()
        {
            double pi = 0;
            double denominator = 1;
            int sign = 1;
            int iterations = 1000000; // Достаточно для точности до 4 знаков

            for (int i = 0; i < iterations; i++)
            {
                pi += sign * (4.0 / denominator);
                denominator += 2;
                sign *= -1;

                // Обновляем прогресс-бар каждые 10000 итераций
                if (i % 10000 == 0)
                {
                    int progress = (int)((i * 100) / iterations);
                    // Invoke нужен для изменения элементов формы из другого потока
                    Invoke(new Action(() => progressBar.Value = progress));
                }
            }

            // Выводим финальный результат
            string finalPi = Math.Round(pi, 4).ToString();
            Invoke(new Action(() => {
                lblResult.Text = "Результат: " + finalPi;
                progressBar.Value = 100;
                btnCalculate.Enabled = true;
                MessageBox.Show("Вычисление завершено!");
            }));
        }
    }

    static class Program
    {
        [STAThread]
        static void Main() { Application.Run(new Form1()); }
    }
}