using System.Data;
using System.Windows.Forms;
using System.IO;

namespace Lab8_Var5
{
    public class Form1 : Form
    {
        private DataGridView dgv = new DataGridView { Dock = DockStyle.Top, Height = 280 };
        private TextBox txtSearch = new TextBox { Location = new Point(10, 290), Width = 220, PlaceholderText = "Наименование или год" };
        private Button btnSearch = new Button { Text = "Поиск", Location = new Point(240, 288), Width = 80 };
        private Button btnSort   = new Button { Text = "По году ↑", Location = new Point(330, 288), Width = 90 };
        private Button btnReset  = new Button { Text = "Сбросить", Location = new Point(430, 288), Width = 90 };

        private DataSet ds = new DataSet();

        public Form1()
        {
            Text = "Транспорт — вариант 5";
            Width = 760; Height = 370;
            Controls.AddRange(new Control[] { dgv, txtSearch, btnSearch, btnSort, btnReset });

            if (File.Exists("transport.xml"))
            {
                ds.ReadXml("transport.xml");
                dgv.DataSource = ds.Tables[0];
                SetHeaders();
            }
            else
            {
                MessageBox.Show("Файл transport.xml не найден рядом с exe.");
            }

            btnSearch.Click += (s, e) =>
            {
                string f = txtSearch.Text.Trim();
                ds.Tables[0].DefaultView.RowFilter = string.IsNullOrEmpty(f)
                    ? ""
                    : $"Name LIKE '%{f}%' OR Year LIKE '%{f}%'";
                dgv.DataSource = ds.Tables[0].DefaultView;
            };

            btnSort.Click += (s, e) =>
            {
                ds.Tables[0].DefaultView.Sort = "Year ASC";
                dgv.DataSource = ds.Tables[0].DefaultView;
            };

            btnReset.Click += (s, e) =>
            {
                ds.Tables[0].DefaultView.RowFilter = "";
                ds.Tables[0].DefaultView.Sort = "";
                txtSearch.Clear();
                dgv.DataSource = ds.Tables[0].DefaultView;
            };
        }

        private void SetHeaders()
        {
            if (dgv.Columns.Count < 7) return;
            string[] headers = { "Наименование", "Тип", "Год выпуска", "Макс. скорость", "Объём двигателя", "Расход (л/100км)", "Объём бака (л)" };
            int[]    widths  = { 170, 110, 90, 110, 120, 130, 110 };
            for (int i = 0; i < headers.Length; i++)
            {
                dgv.Columns[i].HeaderText = headers[i];
                dgv.Columns[i].Width = widths[i];
            }
        }
    }

    static class Program
    {
        [STAThread]
        static void Main() => Application.Run(new Form1());
    }
}
