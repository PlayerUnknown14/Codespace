using System;
using System.IO;
using System.Windows.Forms;
using System.Drawing;

namespace FileBrowserApp
{
    public class Form1 : Form
    {
        // Элементы управления
        private TreeView tvDrives = new TreeView  { Location = new Point(10, 40), Size = new Size(190, 420) };
        private ListBox lbFiles = new ListBox { Location = new Point(210, 58), Size = new Size(180, 420) };

        private Label lblInfo = new Label { Location = new Point(400, 40), Size = new Size(360, 120), BorderStyle = BorderStyle.FixedSingle };
        private TextBox  txtNewPath = new TextBox   { Location = new Point(400, 180), Size = new Size(360, 22) };
        private Button btnUp = new Button { Text = "▲ Вверх", Location = new Point(10, 10), Size = new Size(90, 26) };
        private Button btnCreate = new Button { Text = "Новая папка", Location = new Point(110, 10), Size = new Size(100, 26) };
        private Button btnCopy = new Button { Text = "Копировать", Location = new Point(400, 220), Size = new Size(85, 26) };
        private Button btnMove = new Button { Text = "Переместить", Location = new Point(493, 220), Size = new Size(85, 26) };
        private Button btnRename = new Button { Text = "Переименовать", Location = new Point(586, 220), Size = new Size(110, 26) };
        private Button btnDelete = new Button { Text = "Удалить", Location = new Point(400, 260), Size = new Size(85, 26) };
        private Button btnDrives = new Button { Text = "О дисках", Location = new Point(493, 260), Size = new Size(85, 26) };
        private Button btnAbout = new Button { Text = "О программе", Location = new Point(586, 260), Size = new Size(110, 26) };
        private Label lblFilesList = new Label { Text = "Файлы", Location = new Point(210, 40), AutoSize = true };
        private Label lblPath = new Label { Text = "Путь назначения:", Location = new Point(400, 160), AutoSize = true };

        private string currentPath = "";

        // Конструктор
        public Form1()
        {
            Text = "Браузер файлов — Лабораторная работа №7";
            Size = new Size(790, 510);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            MaximizeBox = false;

            Controls.AddRange(new Control[] {
                tvDrives, lbFiles, lblInfo,
                lblPath, txtNewPath, btnUp, btnCreate,
                btnCopy, btnMove, btnRename, btnDelete,
                btnDrives, btnAbout, lblFilesList
            });

            // Обработчики событий
            tvDrives.AfterSelect += (s, e) => LoadFolder(e.Node.Tag?.ToString() ?? "");
            tvDrives.BeforeExpand += OnTreeExpand;
            lbFiles.SelectedIndexChanged += ShowFileInfo;
            btnUp.Click += (s, e) => { var p = Directory.GetParent(currentPath); if (p != null) LoadFolder(p.FullName); };
            btnCreate.Click += CreateFolder;
            btnCopy.Click += CopyFile;
            btnMove.Click += MoveFile;
            btnRename.Click += RenameFile;
            btnDelete.Click += DeleteFile;
            btnDrives.Click += ShowDrivesInfo;
            btnAbout.Click += (s, e) => ShowAbout();

            LoadDrives();
        }

        // Загрузка дисков в TreeView
        private void LoadDrives()
        {
            tvDrives.Nodes.Clear();
            foreach (var d in DriveInfo.GetDrives())
            {
                if (!d.IsReady) continue;
                var node = new TreeNode(d.Name) { Tag = d.RootDirectory.FullName };
                node.Nodes.Add(new TreeNode("...")); // заглушка для стрелки раскрытия
                tvDrives.Nodes.Add(node);
            }
        }

        private void OnTreeExpand(object? s, TreeViewCancelEventArgs e)
        {
            e.Node.Nodes.Clear();
            string path = e.Node.Tag?.ToString() ?? "";
            try {
                foreach (var d in Directory.GetDirectories(path))
                {
                    var child = new TreeNode(Path.GetFileName(d)) { Tag = d };
                    try { if (Directory.GetDirectories(d).Length > 0) child.Nodes.Add(new TreeNode("...")); } catch { }
                    e.Node.Nodes.Add(child);
                }
            } catch { }
        }

        // Загрузка содержимого папки
        private void LoadFolder(string path)
        {
            if (!Directory.Exists(path)) return;
            currentPath = path;
            lbFiles.Items.Clear();
            lblInfo.Text = "";
            txtNewPath.Text = path;

            try {
                foreach (var f in new DirectoryInfo(path).GetFiles()) lbFiles.Items.Add(f.Name);
            } catch (Exception ex) { MessageBox.Show("Ошибка: " + ex.Message); }
        }

        // Информация о выбранном файле
        private void ShowFileInfo(object? s, EventArgs e)
        {
            if (lbFiles.SelectedItem == null) return;
            try {
                var fi = new FileInfo(Path.Combine(currentPath, lbFiles.SelectedItem.ToString()!));
                lblInfo.Text = $"Название:      {fi.Name}\n" +
                                $"Размер:   {fi.Length:N0} байт\n" +
                                $"Создан:   {fi.CreationTime:dd.MM.yyyy HH:mm}\n" +
                                $"Изменён:  {fi.LastWriteTime:dd.MM.yyyy HH:mm}\n" +
                                $"Доступ:   {fi.LastAccessTime:dd.MM.yyyy HH:mm}\n" +
                                $"Атрибуты: {fi.Attributes}";
                txtNewPath.Text = fi.FullName;
            } catch (Exception ex) { MessageBox.Show("Ошибка: " + ex.Message); }
        }

        // Операции с файлами
        private void CreateFolder(object? s, EventArgs e)
        {
            string name = Prompt("Название новой папки:", "Создание папки");
            if (string.IsNullOrEmpty(name)) return;
            try { Directory.CreateDirectory(Path.Combine(currentPath, name)); LoadFolder(currentPath); }
            catch (Exception ex) { MessageBox.Show("Ошибка: " + ex.Message); }
        }

        private void CopyFile(object? s, EventArgs e)
        {
            if (lbFiles.SelectedItem == null) { MessageBox.Show("Выберите файл."); return; }
            try { File.Copy(Path.Combine(currentPath, lbFiles.SelectedItem.ToString()!), txtNewPath.Text, true); LoadFolder(currentPath); }
            catch (Exception ex) { MessageBox.Show("Ошибка: " + ex.Message); }
        }

        private void MoveFile(object? s, EventArgs e)
        {
            if (lbFiles.SelectedItem == null) { MessageBox.Show("Выберите файл."); return; }
            try { File.Move(Path.Combine(currentPath, lbFiles.SelectedItem.ToString()!), txtNewPath.Text, true); LoadFolder(currentPath); }
            catch (Exception ex) { MessageBox.Show("Ошибка: " + ex.Message); }
        }

        private void RenameFile(object? s, EventArgs e)
        {
            if (lbFiles.SelectedItem == null) { MessageBox.Show("Выберите файл."); return; }
            string newName = Prompt("Новое имя файла:", "Переименование", lbFiles.SelectedItem.ToString()!);
            if (string.IsNullOrEmpty(newName)) return;
            try {
                File.Move(Path.Combine(currentPath, lbFiles.SelectedItem.ToString()!), Path.Combine(currentPath, newName));
                LoadFolder(currentPath);
            } catch (Exception ex) { MessageBox.Show("Ошибка: " + ex.Message); }
        }

        private void DeleteFile(object? s, EventArgs e)
        {
            if (lbFiles.SelectedItem == null) { MessageBox.Show("Выберите файл."); return; }
            string name = lbFiles.SelectedItem.ToString()!;
            if (MessageBox.Show($"Удалить «{name}»?", "Подтверждение", MessageBoxButtons.YesNo) != DialogResult.Yes) return;
            try { File.Delete(Path.Combine(currentPath, name)); LoadFolder(currentPath); }
            catch (Exception ex) { MessageBox.Show("Ошибка: " + ex.Message); }
        }

        // Информация о дисках
        private void ShowDrivesInfo(object? s, EventArgs e)
        {
            string info = "";
            foreach (var d in DriveInfo.GetDrives())
            {
                if (d.IsReady)
                    info += $"{d.Name}  [{d.VolumeLabel}]  {d.DriveFormat}  " +
                            $"Всего: {d.TotalSize/1024/1024/1024} ГБ  " +
                            $"Свободно: {d.AvailableFreeSpace/1024/1024/1024} ГБ\n";
                else
                    info += $"{d.Name}  [не готов]\n";
            }
            MessageBox.Show(info, "Информация о логических дисках");
        }

        // Диалог «О программе»
        private void ShowAbout()
        {
            MessageBox.Show(
                "Браузер файлов\n\n" +
                "Лабораторная работа №7\n" +
                "Тема: Работа с файловой системой\n",
                "О программе",
                MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        // Вспомогательный диалог ввода
        private string Prompt(string text, string title, string defaultVal = "")
        {
            var f = new Form  { Text = title, Size = new Size(380, 130), StartPosition = FormStartPosition.CenterParent, FormBorderStyle = FormBorderStyle.FixedDialog };
            var lbl = new Label { Text = text, Left = 10, Top = 12, AutoSize = true };
            var tb = new TextBox { Left = 10, Top = 32, Width = 348, Text = defaultVal };
            var ok = new Button  { Text = "OK", Left = 190, Top = 62, Size = new Size(75, 26), DialogResult = DialogResult.OK };
            var can = new Button  { Text = "Отмена", Left = 274, Top = 62, Size = new Size(85, 26), DialogResult = DialogResult.Cancel };
            f.Controls.AddRange(new Control[] { lbl, tb, ok, can });
            f.AcceptButton = ok; f.CancelButton = can;
            return f.ShowDialog() == DialogResult.OK ? tb.Text.Trim() : "";
        }
    }

    // Точка входа
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
