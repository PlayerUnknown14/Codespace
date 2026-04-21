using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

namespace GraphicsEditor
{
    static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }

    public class MainForm : Form
    {
        // Компоненты интерфейса
        private MenuStrip menuStrip;
        private ToolStrip toolStrip;
        private PictureBox pictureBox;
        private StatusStrip statusStrip;
        private ToolStripStatusLabel statusLabel;

        // Диалоги
        private ColorDialog colorDialog;
        private OpenFileDialog openFileDialog;
        private SaveFileDialog saveFileDialog;

        // Графика
        private Bitmap bitmap;
        private Graphics graphics;
        private Point startPoint;
        private bool isDrawing = false;

        // Настройки рисования
        private Color penColor = Color.Black;
        private float penWidth = 2f;
        private DashStyle penStyle = DashStyle.Solid;
        private Color brushColor = Color.Black;
        private FillStyle brushStyle = FillStyle.Solid;
        private string currentFigure = "Линия";

        // Перечисления
        private enum FillStyle { Solid, Hatch, None }

        public MainForm()
        {
            InitializeComponent();
            InitializeGraphics();
        }

        private void InitializeComponent()
        {
            // Настройка формы
            this.Text = "Простой графический редактор";
            this.Size = new Size(1000, 700);
            this.StartPosition = FormStartPosition.CenterScreen;

            // Меню
            menuStrip = new MenuStrip();
            var fileMenu = new ToolStripMenuItem("Файл");
            var newMenuItem = new ToolStripMenuItem("Новый");
            var openMenuItem = new ToolStripMenuItem("Открыть");
            var saveMenuItem = new ToolStripMenuItem("Сохранить");
            var exitMenuItem = new ToolStripMenuItem("Выход");
            
            var toolsMenu = new ToolStripMenuItem("Инструменты");
            var figureMenu = new ToolStripMenuItem("Фигура");
            var lineItem = new ToolStripMenuItem("Линия");
            var rectItem = new ToolStripMenuItem("Прямоугольник");
            var ellipseItem = new ToolStripMenuItem("Эллипс");
            var penColorItem = new ToolStripMenuItem("Цвет пера");
            var penWidthItem = new ToolStripMenuItem("Толщина пера");
            var brushColorItem = new ToolStripMenuItem("Цвет кисти");
            var brushStyleItem = new ToolStripMenuItem("Стиль кисти");

            var helpMenu = new ToolStripMenuItem("Помощь");
            var aboutMenuItem = new ToolStripMenuItem("О программе");

            fileMenu.DropDownItems.AddRange(new ToolStripItem[] { newMenuItem, openMenuItem, saveMenuItem, new ToolStripSeparator(), exitMenuItem });
            figureMenu.DropDownItems.AddRange(new ToolStripItem[] { lineItem, rectItem, ellipseItem });
            toolsMenu.DropDownItems.AddRange(new ToolStripItem[] { figureMenu, penColorItem, penWidthItem, brushColorItem, brushStyleItem });
            helpMenu.DropDownItems.Add(aboutMenuItem);
            menuStrip.Items.AddRange(new ToolStripItem[] { fileMenu, toolsMenu, helpMenu });

            // Панель инструментов
            toolStrip = new ToolStrip();
            var newToolBtn = new ToolStripButton("Создать", null, (s, e) => NewImage());
            var openToolBtn = new ToolStripButton("Открыть", null, (s, e) => OpenImage());
            var saveToolBtn = new ToolStripButton("Сохранить", null, (s, e) => SaveImage());
            var colorToolBtn = new ToolStripButton("Выбор цвета", null, (s, e) => SelectPenColor());
            var figureCombo = new ToolStripComboBox();
            figureCombo.Items.AddRange(new object[] { "Линия", "Прямоугольник", "Эллипс" });
            figureCombo.SelectedIndex = 0;
            figureCombo.SelectedIndexChanged += (s, e) => currentFigure = figureCombo.SelectedItem.ToString();

            toolStrip.Items.AddRange(new ToolStripItem[] { newToolBtn, openToolBtn, saveToolBtn, new ToolStripSeparator(), colorToolBtn, figureCombo });

            // Область рисования
            pictureBox = new PictureBox();
            pictureBox.Dock = DockStyle.Fill;
            pictureBox.BackColor = Color.White;
            pictureBox.Cursor = Cursors.Cross;
            pictureBox.MouseDown += PictureBox_MouseDown;
            pictureBox.MouseMove += PictureBox_MouseMove;
            pictureBox.MouseUp += PictureBox_MouseUp;

            // Статусная строка
            statusStrip = new StatusStrip();
            statusLabel = new ToolStripStatusLabel("Готов к работе");
            statusStrip.Items.Add(statusLabel);

            // Диалоги
            colorDialog = new ColorDialog();
            openFileDialog = new OpenFileDialog();
            openFileDialog.Filter = "Файлы изображения|*.bmp;*.gif;*.jpeg;*.jpg;*.png;*.tiff";
            saveFileDialog = new SaveFileDialog();
            saveFileDialog.Filter = "JPEG изображение|*.jpg|PNG изображение|*.png|Bitmap|*.bmp";

            // Добавление элементов
            this.Controls.Add(pictureBox);
            this.Controls.Add(toolStrip);
            this.Controls.Add(menuStrip);
            this.Controls.Add(statusStrip);

            // Привязка событий меню
            newMenuItem.Click += (s, e) => NewImage();
            openMenuItem.Click += (s, e) => OpenImage();
            saveMenuItem.Click += (s, e) => SaveImage();
            exitMenuItem.Click += (s, e) => this.Close();
            penColorItem.Click += (s, e) => SelectPenColor();
            penWidthItem.Click += (s, e) => SelectPenWidth();
            brushColorItem.Click += (s, e) => SelectBrushColor();
            brushStyleItem.Click += (s, e) => SelectBrushStyle();
            aboutMenuItem.Click += (s, e) => ShowAbout();
            lineItem.Click += (s, e) => { currentFigure = "Линия"; figureCombo.SelectedItem = "Линия"; };
            rectItem.Click += (s, e) => { currentFigure = "Прямоугольник"; figureCombo.SelectedItem = "Прямоугольник"; };
            ellipseItem.Click += (s, e) => { currentFigure = "Эллипс"; figureCombo.SelectedItem = "Эллипс"; };
        }

        private void InitializeGraphics()
        {
            bitmap = new Bitmap(pictureBox.ClientSize.Width, pictureBox.ClientSize.Height);
            graphics = Graphics.FromImage(bitmap);
            graphics.Clear(Color.White);
            pictureBox.Image = bitmap;
        }

        // События рисования
        private void PictureBox_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isDrawing = true;
                startPoint = e.Location;
                statusLabel.Text = $"Рисование: {currentFigure}";
            }
        }

        private void PictureBox_MouseMove(object sender, MouseEventArgs e)
        {
            if (isDrawing)
            {
                statusLabel.Text = $"Координаты: X={e.X}, Y={e.Y}";
            }
        }

        private void PictureBox_MouseUp(object sender, MouseEventArgs e)
        {
            if (isDrawing && e.Button == MouseButtons.Left)
            {
                isDrawing = false;
                DrawFigure(startPoint, e.Location);
                pictureBox.Invalidate();
                statusLabel.Text = "Готов к работе";
            }
        }

        private void DrawFigure(Point start, Point end)
        {
            using (Pen pen = new Pen(penColor, penWidth) { DashStyle = penStyle })
            {
                int width = end.X - start.X;
                int height = end.Y - start.Y;

                switch (currentFigure)
                {
                    case "Линия":
                        graphics.DrawLine(pen, start, end);
                        break;
                    case "Прямоугольник":
                        graphics.DrawRectangle(pen, start.X, start.Y, width, height);
                        if (brushStyle != FillStyle.None)
                            FillRectangle(start.X, start.Y, width, height);
                        break;
                    case "Эллипс":
                        graphics.DrawEllipse(pen, start.X, start.Y, width, height);
                        if (brushStyle != FillStyle.None)
                            FillEllipse(start.X, start.Y, width, height);
                        break;
                }
            }
        }

        private void FillRectangle(int x, int y, int w, int h)
        {
            using (Brush brush = CreateBrush())
            {
                graphics.FillRectangle(brush, x, y, w, h);
            }
        }

        private void FillEllipse(int x, int y, int w, int h)
        {
            using (Brush brush = CreateBrush())
            {
                graphics.FillEllipse(brush, x, y, w, h);
            }
        }

        private Brush CreateBrush()
        {
            if (brushStyle == FillStyle.Hatch)
                return new HatchBrush(HatchStyle.Cross, brushColor, Color.White);
            return new SolidBrush(brushColor);
        }

        // Функции меню
        private void NewImage()
        {
            graphics.Clear(Color.White);
            pictureBox.Invalidate();
            statusLabel.Text = "Создано новое изображение";
        }

        private void OpenImage()
        {
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    graphics.Clear(Color.White);
                    using (Image img = Image.FromFile(openFileDialog.FileName))
                    {
                        graphics.DrawImage(img, Point.Empty);
                    }
                    pictureBox.Invalidate();
                    statusLabel.Text = $"Открыто: {openFileDialog.FileName}";
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Ошибка загрузки: {ex.Message}", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }

        private void SaveImage()
        {
            if (saveFileDialog.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    string ext = System.IO.Path.GetExtension(saveFileDialog.FileName).ToLower();
                    var format = ext switch
                    {
                        ".png" => System.Drawing.Imaging.ImageFormat.Png,
                        ".bmp" => System.Drawing.Imaging.ImageFormat.Bmp,
                        _ => System.Drawing.Imaging.ImageFormat.Jpeg
                    };
                    bitmap.Save(saveFileDialog.FileName, format);
                    statusLabel.Text = $"Сохранено: {saveFileDialog.FileName}";
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Ошибка сохранения: {ex.Message}", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }

        private void SelectPenColor()
        {
            colorDialog.Color = penColor;
            if (colorDialog.ShowDialog() == DialogResult.OK)
            {
                penColor = colorDialog.Color;
                statusLabel.Text = $"Цвет пера: {penColor.Name}";
            }
        }

        private void SelectPenWidth()
        {
            string input = Microsoft.VisualBasic.Interaction.InputBox("Введите толщину пера:", "Толщина пера", penWidth.ToString());
            if (float.TryParse(input, out float w) && w > 0)
            {
                penWidth = w;
                statusLabel.Text = $"Толщина пера: {penWidth}";
            }
        }

        private void SelectBrushColor()
        {
            colorDialog.Color = brushColor;
            if (colorDialog.ShowDialog() == DialogResult.OK)
            {
                brushColor = colorDialog.Color;
                statusLabel.Text = $"Цвет кисти: {brushColor.Name}";
            }
        }

        private void SelectBrushStyle()
        {
            var result = MessageBox.Show("Выберите стиль кисти:\nДа - Заштрихованная\nНет - Сплошная\nОтмена - Без заливки", 
                "Стиль кисти", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Question);
            
            if (result == DialogResult.Yes)
                brushStyle = FillStyle.Hatch;
            else if (result == DialogResult.No)
                brushStyle = FillStyle.Solid;
            else
                brushStyle = FillStyle.None;
                
            statusLabel.Text = $"Стиль кисти: {brushStyle}";
        }

        private void ShowAbout()
        {
            MessageBox.Show(
                "Графический редактор\n" +
                "Лабораторная работа №6, Вариант №5\n" +
                "Выполнил: Студент группы БПИ24-02, Гордов В.\n",
                "О программе",
                MessageBoxButtons.OK,
                MessageBoxIcon.Information);
        }

        // Сохранение состояния при изменении размеров
        protected override void OnResize(EventArgs e)
        {
            base.OnResize(e);
            // Пересоздаем битмап при изменении размера формы, чтобы сохранить рисунок
            if (bitmap != null && pictureBox.ClientSize.Width > 0 && pictureBox.ClientSize.Height > 0)
            {
                Bitmap oldBitmap = bitmap;
                Bitmap newBitmap = new Bitmap(pictureBox.ClientSize.Width, pictureBox.ClientSize.Height);
                using (Graphics g = Graphics.FromImage(newBitmap))
                {
                    g.Clear(Color.White);
                    g.DrawImage(oldBitmap, Point.Empty);
                }
                bitmap = newBitmap;
                graphics = Graphics.FromImage(bitmap);
                pictureBox.Image = bitmap;
                oldBitmap.Dispose();
            }
        }

        protected override void OnFormClosing(FormClosingEventArgs e)
        {
            bitmap?.Dispose();
            graphics?.Dispose();
            base.OnFormClosing(e);
        }
    }
}