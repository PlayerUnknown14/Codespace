using System;
using System.Data;
using System.Windows.Forms;
using System.IO;

namespace Lab8_Var12
{
    public class Form1 : Form
    {
        private DataGridView dgv = new DataGridView { Dock = DockStyle.Top, Height = 300 };
        private TextBox txtSearch = new TextBox { Location = new Point(10, 320), Width = 200 };
        private Button btnSearch = new Button { Text = "Поиск (Область)", Location = new Point(220, 318) };
        private Button btnSort = new Button { Text = "Сортировать по названию", Location = new Point(10, 360), Width = 200 };
        
        private DataSet ds = new DataSet();

        public Form1()
        {
            Text = "Научные разработки (Вар. 12)";
            Width = 600; Height = 450;
            Controls.AddRange(new Control[] { dgv, txtSearch, btnSearch, btnSort });

            // Загрузка XML
            if (File.Exists("research.xml"))
            {
                ds.ReadXml("research.xml");
                dgv.DataSource = ds.Tables[0];
            }

            btnSearch.Click += (s, e) => {
                DataTable dt = ds.Tables[0];
                string filter = txtSearch.Text;

                if (string.IsNullOrWhiteSpace(filter)) 
                {
                    dt.DefaultView.RowFilter = ""; // Сброс фильтра
                }
                else
                {
                    // Поиск по нескольким полям сразу (Название или Область или Дата)
                    // Используем 'LIKE' для частичного совпадения
                    dt.DefaultView.RowFilter = 
                        $"Name LIKE '%{filter}%' OR " +
                        $"Area LIKE '%{filter}%' OR " +
                        $"EndDate LIKE '%{filter}%'"; 
                }
            };

            btnSort.Click += (s, e) => {
                // Сортировка по полю Name
                (dgv.DataSource as DataTable).DefaultView.Sort = "Name ASC";
            };
        }
    }

    static class Program
    {
        [STAThread]
        static void Main() { Application.Run(new Form1()); }
    }
}