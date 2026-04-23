using System.Drawing;

namespace Lab5_Variant5
{
    public class FormInput : Form
    {
        // Вводимые числа
        public double Number1 { get; private set; }
        public double Number2 { get; private set; }
        public double Number3 { get; private set; }
        // Флаги режимов вычислений
        public bool IsSumm { get; private set; }
        public bool IsMultiply { get; private set; }

        // Текстовые поля и кнопки для ввода данных
        private TextBox textBox1, textBox2, textBox3;
        private CheckBox checkBoxSumm, checkBoxMultiply;
        private Button buttonOK;
        // Метки для расположения полей ввода
        private Label label1, label2, label3;

        public FormInput()
        {
            this.Text = "Ввод данных";
            this.Size = new Size(350, 350);
            this.StartPosition = FormStartPosition.CenterParent;
            this.FormBorderStyle = FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;

            // Инициализация элементов интерфейса
            int labelH = 20;
            int labelW = 120;
            int labelX = 10;
            int labelY = 20;
            int boxW = 180;

            label1 = new Label() { Text = "Число №1:", Location = new Point(labelX, labelY), Size = new Size(labelW, labelH) };
            textBox1 = new TextBox() { Location = new Point(labelW + 10, labelH), Size = new Size(boxW, 20) };
            
            label2 = new Label() { Text = "Число №2:", Location = new Point(labelX, labelY + 30), Size = new Size(labelW, labelH) };
            textBox2 = new TextBox() { Location = new Point(labelW + 10, labelH + 30), Size = new Size(boxW, 20) };

            label3 = new Label() { Text = "Число №3:", Location = new Point(labelX, labelY + 60), Size = new Size(labelW, labelH) };
            textBox3 = new TextBox() { Location = new Point(labelW + 10, labelH + 60), Size = new Size(boxW, 20) };

            checkBoxSumm = new CheckBox() { Text = "Сумма", Location = new Point(labelX, labelY + 100) };
            checkBoxMultiply = new CheckBox() { Text = "Произведение", Location = new Point(labelX, labelY + 130) };

            buttonOK = new Button() { Text = "Принять", Location = new Point(100, labelH + 180), Size = new Size(100, 30) };
            buttonOK.Click += ButtonOK_Click;

            // Добавляем элементы на форму
            this.Controls.Add(label1); 
            this.Controls.Add(textBox1);
            this.Controls.Add(label2); 
            this.Controls.Add(textBox2);
            this.Controls.Add(label3); 
            this.Controls.Add(textBox3);
            this.Controls.Add(checkBoxSumm);
            this.Controls.Add(checkBoxMultiply);
            this.Controls.Add(buttonOK);
        }

        // Обработчик событий для кнопки подтвеждения (и выхода из окна ввода)
        private void ButtonOK_Click(object? sender, EventArgs e)
        {
            // Проверки на коррекность всех полей
            if (!double.TryParse(textBox1.Text, out double num1) || !double.TryParse(textBox2.Text, out double num2) || !double.TryParse(textBox3.Text, out double num3))
            {
                MessageBox.Show("Одно или несколько полей ввода пусты или не содержат число.", "Ошибка");
                return;
            }
            if (!checkBoxSumm.Checked && !checkBoxMultiply.Checked)
            {
                MessageBox.Show("Не выбран ни один режим вычислений.", "Ошибка");
                return;
            }

            Number1 = num1;
            Number2 = num2;
            Number3 = num3;
            IsSumm = checkBoxSumm.Checked;
            IsMultiply = checkBoxMultiply.Checked;

            this.DialogResult = DialogResult.OK;
            this.Close();
        }
    }
}