using System;
using System.Drawing;
using System.Windows.Forms;

namespace Lab5_Var12
{
    // --- ГЛАВНАЯ ФОРМА ---
    public class Form1 : Form
    {
        private MenuStrip menuStrip1 = new MenuStrip();
        private ToolStripMenuItem menuInput = new ToolStripMenuItem("Input");
        private ToolStripMenuItem menuShow = new ToolStripMenuItem("Show");
        private ToolStripMenuItem menuExit = new ToolStripMenuItem("Exit");

        // Переменные для данных
        private double x1, y1, x2, y2;
        private bool needLen, needKoef;

        public Form1()
        {
            Text = "Главное окно (Вар. 12)";
            Width = 400; Height = 300;

            menuShow.Enabled = false; // По заданию недоступно сразу

            menuInput.Click += (s, e) => {
                Form2 dlg = new Form2();
                if (dlg.ShowDialog() == DialogResult.OK)
                {
                    x1 = dlg.X1; y1 = dlg.Y1; x2 = dlg.X2; y2 = dlg.Y2;
                    needLen = dlg.NeedLen; needKoef = dlg.NeedKoef;
                    menuShow.Enabled = true;
                }
            };

            menuShow.Click += (s, e) => {
                string res = "";
                if (needLen) res += "Длина: " + Math.Sqrt(Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2)).ToString("F2") + "\n";
                if (needKoef) res += "Коэф: " + (Math.Abs(x2 - x1) < 0.001 ? "Inf" : ((y2 - y1) / (x2 - x1)).ToString("F2"));
                MessageBox.Show(res, "Результат");
                menuShow.Enabled = false;
            };

            menuExit.Click += (s, e) => Application.Exit();

            menuStrip1.Items.AddRange(new ToolStripItem[] { menuInput, menuShow, menuExit });
            MainMenuStrip = menuStrip1;
            Controls.Add(menuStrip1);
        }
    }

    // --- ВТОРАЯ ФОРМА (ВВОД ДАННЫХ) ---
    public class Form2 : Form
    {
        private TextBox txtX1 = new TextBox() { Left = 50, Top = 20, Width = 50 };
        private TextBox txtY1 = new TextBox() { Left = 110, Top = 20, Width = 50 };
        private TextBox txtX2 = new TextBox() { Left = 50, Top = 50, Width = 50 };
        private TextBox txtY2 = new TextBox() { Left = 110, Top = 50, Width = 50 };
        private CheckBox chbLen = new CheckBox() { Text = "length", Left = 200, Top = 20 };
        private CheckBox chbKoef = new CheckBox() { Text = "koef", Left = 200, Top = 50 };
        private Button btnOk = new Button() { Text = "OK", Left = 100, Top = 100 };

        public double X1 => double.Parse(txtX1.Text);
        public double Y1 => double.Parse(txtY1.Text);
        public double X2 => double.Parse(txtX2.Text);
        public double Y2 => double.Parse(txtY2.Text);
        public bool NeedLen => chbLen.Checked;
        public bool NeedKoef => chbKoef.Checked;

        public Form2()
        {
            Text = "Ввод данных"; Width = 350; Height = 200;
            Controls.AddRange(new Control[] { txtX1, txtY1, txtX2, txtY2, chbLen, chbKoef, btnOk });
            btnOk.Click += (s, e) => { DialogResult = DialogResult.OK; Close(); };
        }
    }

    static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.Run(new Form1());
        }
    }
}