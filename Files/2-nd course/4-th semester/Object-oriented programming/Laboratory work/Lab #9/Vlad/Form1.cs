using System;
using System.Threading;
using System.Windows.Forms;
using System.Drawing;

namespace Lab9_Var5
{
    public class Form1 : Form
    {
        private Label lblX = new Label { Text = "Введите x = [-1; 1]:", Location = new Point(20, 22), Width = 160 };
        private TextBox txtX = new TextBox { Location = new Point(180, 20), Width = 120 };
        private Button btnCalc = new Button { Text = "Вычислить", Location = new Point(20, 55), Width = 120 };
        private Label lblResult = new Label { Location = new Point(20, 95), Width = 340, Text = "Ожидание ввода..." };
        private ProgressBar bar = new ProgressBar { Location = new Point(20, 125), Width = 340, Minimum = 0, Maximum = 100 };

        public Form1()
        {
            Text = "Вариант 5: ln(1-x)";
            Width = 400; Height = 210;
            Controls.AddRange(new Control[] { lblX, txtX, btnCalc, lblResult, bar });
            btnCalc.Click += (s, e) =>
            {
                if (!double.TryParse(txtX.Text.Replace('.', ','), out double x) || x < -1 || x > 1)
                {
                    lblResult.Text = "x не в интервале!";
                    return;
                }
                btnCalc.Enabled = false;
                lblResult.Text = "Вычисляется...";
                bar.Value = 0;
                new Thread(() => Calculate(x)) { IsBackground = true }.Start();
            };
        }

        private void Calculate(double x)
        {
            const double eps = 1e-5;
            double sum = 0;
            double term = -x;
            int n = 1;

            while (Math.Abs(term) >= eps)
            {
                sum += term;
                n++;
                term *= x * (n - 1.0) / n;

                if (n % 200 == 0)
                {
                    double progress = Math.Min(99, eps / Math.Abs(term) * 99);
                    Invoke(new Action(() => bar.Value = (int)progress));
                }
            }
            sum += term;

            string result = Math.Round(sum, 5).ToString("F5");
            Invoke(new Action(() =>
            {
                lblResult.Text = $"ln(1 - {txtX.Text}) ≈ {result} (итераций: {n})";
                bar.Value = 100;
                btnCalc.Enabled = true;
            }));
        }
    }

    static class Program
    {
        [STAThread]
        static void Main() { Application.Run(new Form1()); }
    }
}