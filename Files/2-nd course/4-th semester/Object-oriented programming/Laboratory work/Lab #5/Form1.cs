using System;
using System.Windows.Forms;

namespace Lab5_Variant5
{
    public partial class Form1 : Form
    {
        // Переменные для хранения данных, полученных из Form2
        double n1, n2, n3;
        bool mustSum, mustMul;

        public Form1()
        {
            InitializeComponent();
        }

        // Обработка нажатия "Input"
        private void inputToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form2 f2 = new Form2();

            // Открываем как диалог
            if (f2.ShowDialog() == DialogResult.OK)
            {
                // Забираем данные из свойств Form2
                n1 = f2.N1;
                n2 = f2.N2;
                n3 = f2.N3;
                mustSum = f2.DoSum;
                mustMul = f2.DoMul;

                // Делаем команду Calc доступной
                calcToolStripMenuItem.Enabled = true;
            }
        }

        // Обработка нажатия "Calc"
        private void calcToolStripMenuItem_Click(object sender, EventArgs e)
        {
            string result = "Результаты вычислений:\n\n";

            if (mustSum)
            {
                double sum = n1 + n2 + n3;
                result += $"Сумма трех чисел: {sum}\n";
            }

            if (mustMul)
            {
                double mul = n1 * n2;
                result += $"Произведение первых двух: {mul}\n";
            }

            if (!mustSum && !mustMul)
            {
                result = "Вы не выбрали ни одного режима вычислений (флажки не отмечены).";
            }

            // Вывод результата в окно сообщений
            MessageBox.Show(result, "Результат");
        }

        // Обработка нажатия "About"
        private void aboutToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Разработчик: Иванов И.И.\nГруппа: ЭВМ-23\nВариант №5", "О программе");
        }
    }
}