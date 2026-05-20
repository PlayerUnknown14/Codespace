using System;
using System.Drawing;
using System.Windows.Forms;
using System.Drawing.Imaging;

namespace SimpleGraphicEditor
{
    public class Form1 : Form
    {
        private Bitmap bmp;
        private Graphics g;
        private Point startPoint;
        private PictureBox pb = new PictureBox { Dock = DockStyle.Fill, BackColor = Color.White };
        private ComboBox figureList = new ComboBox { Items = { "Линия", "Прямоугольник", "Эллипс" }, SelectedIndex = 0 };

        public Form1()
        {
            Text = "Графический редактор";
            Width = 800; Height = 600;
            
            // Инициализация графики
            bmp = new Bitmap(800, 600);
            g = Graphics.FromImage(bmp);
            pb.Image = bmp;

            // Меню
            MenuStrip ms = new MenuStrip();
            ToolStripMenuItem file = new ToolStripMenuItem("Файл");
            file.DropDownItems.Add("Новый", null, (s, e) => { g.Clear(Color.White); pb.Invalidate(); });
            file.DropDownItems.Add("Сохранить", null, (s, e) => { 
                SaveFileDialog sfd = new SaveFileDialog { Filter = "JPEG|*.jpg" };
                if (sfd.ShowDialog() == DialogResult.OK) bmp.Save(sfd.FileName, ImageFormat.Jpeg);
            });
            file.DropDownItems.Add("О программе", null, (s, e) => MessageBox.Show("Простой графический редактор, Вар. 12"));
            
            ms.Items.Add(file);
            ms.Items.Add(new ToolStripControlHost(figureList));
            
            Controls.Add(pb);
            Controls.Add(ms);

            pb.MouseDown += (s, e) => startPoint = e.Location;
            pb.MouseUp += (s, e) => {
                Pen pen = new Pen(Color.Black, 2);
                if (figureList.SelectedIndex == 0) g.DrawLine(pen, startPoint, e.Location);
                else if (figureList.SelectedIndex == 1) g.DrawRectangle(pen, new Rectangle(startPoint, new Size(e.X - startPoint.X, e.Y - startPoint.Y)));
                else g.DrawEllipse(pen, new Rectangle(startPoint, new Size(e.X - startPoint.X, e.Y - startPoint.Y)));
                pb.Invalidate();
            };
        }
    }

    static class Program
    {
        [STAThread]
        static void Main() { Application.Run(new Form1()); }
    }
}