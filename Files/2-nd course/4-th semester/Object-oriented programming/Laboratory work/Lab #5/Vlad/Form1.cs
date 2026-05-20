namespace Lab5_Variant5
{
    public class Form1 : Form
    {
        private MenuStrip menuStrip;
        private ToolStripMenuItem inputMenuItem;
        private ToolStripMenuItem calcMenuItem;
        private ToolStripMenuItem aboutMenuItem;

        // Переменные для данных
        private double number1, number2, number3;
        private bool isSummSelected, isMultiplySelected;
        private bool isDataValid = false;

        public Form1()
        {
            this.Text = "Лабораторная 5 - Вариант 5";
            this.Size = new System.Drawing.Size(400, 300);
            this.StartPosition = FormStartPosition.CenterScreen;

            // Создание меню и добавляем нужные кнопки
            menuStrip = new MenuStrip();
            
            inputMenuItem = new ToolStripMenuItem("Ввод");
            inputMenuItem.Click += InputMenuItem_Click;
            
            calcMenuItem = new ToolStripMenuItem("Вычисления");
            calcMenuItem.Click += CalcMenuItem_Click;
            calcMenuItem.Enabled = false;

            aboutMenuItem = new ToolStripMenuItem("О программе");
            aboutMenuItem.Click += AboutMenuItem_Click;

            menuStrip.Items.Add(inputMenuItem);
            menuStrip.Items.Add(calcMenuItem);
            menuStrip.Items.Add(aboutMenuItem);

            // Добавляем меню на форму
            this.MainMenuStrip = menuStrip;
            this.Controls.Add(menuStrip);
        }

        // Обработчик событий для ввода данных
        private void InputMenuItem_Click(object? sender, EventArgs e)
        {
            FormInput inputForm = new FormInput();
            if (inputForm.ShowDialog() == DialogResult.OK) // Юзер ввёл все данные в открывшуюся форму?
            {
                number1 = inputForm.Number1;
                number2 = inputForm.Number2;
                number3 = inputForm.Number3;
                isSummSelected = inputForm.IsSumm;
                isMultiplySelected = inputForm.IsMultiply;
                isDataValid = true;
                calcMenuItem.Enabled = true;
            }
        }

        // Обработчик событий для вычисления результатов
        private void CalcMenuItem_Click(object? sender, EventArgs e)
        {
            if (!isDataValid) return;

            string resultText = "";
            if (isSummSelected)
            {
                double sum = number1 + number2 + number3;
                resultText += $"Сумма трёх чисел: {sum}\n";
            }
            if (isMultiplySelected)
            {
                double product = number1 * number2;
                resultText += $"Произведение первых двух: {product}\n";
            }

            FormResult resultForm = new FormResult(resultText);
            resultForm.ShowDialog();
        }

        // Обработчик событий с инфой о разрабе
        private void AboutMenuItem_Click(object? sender, EventArgs e)
        {
            MessageBox.Show("Разработчик: Студент группы БПИ24-02 Гордов В.\nЛабораторная работа №5, Вариант №5", "О программе");
        }
    }
}