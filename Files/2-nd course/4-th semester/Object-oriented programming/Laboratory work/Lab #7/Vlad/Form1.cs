using System;
using System.IO;
using System.Windows.Forms;
using System.Drawing;

namespace FileBrowserApp
{
    public class Form1 : Form
    {
        // ── Элементы управления ──────────────────────────────────────────
        private TreeView tvDrives   = new TreeView  { Location = new Point(10, 40),  Size = new Size(190, 420) };
        private ListBox  lbFolders  = new ListBox   { Location = new Point(210, 40), Size = new Size(180, 200) };
        private ListBox  lbFiles    = new ListBox   { Location = new Point(210, 250), Size = new Size(180, 210) };

        private Label    lblInfo    = new Label     { Location = new Point(400, 40),  Size = new Size(360, 120), BorderStyle = BorderStyle.FixedSingle };
        private TextBox  txtNewPath = new TextBox   { Location = new Point(400, 170), Size = new Size(360, 22)  };

        private Button btnUp        = new Button { Text = "▲ Вверх",      Location = new Point(10,  10),  Size = new Size(90,  26) };
        private Button btnCreate    = new Button { Text = "Новая папка",  Location = new Point(110, 10),  Size = new Size(100, 26) };
        private Button btnCopy      = new Button { Text = "Копировать",   Location = new Point(400, 200), Size = new Size(85,  26) };
        private Button btnMove      = new Button { Text = "Переместить",  Location = new Point(493, 200), Size = new Size(85,  26) };
        private Button btnRename    = new Button { Text = "Переименовать",Location = new Point(586, 200), Size = new Size(110, 26) };
        private Button btnDelete    = new Button { Text = "Удалить",      Location = new Point(400, 234), Size = new Size(85,  26) };
        private Button btnDrives    = new Button { Text = "О дисках",     Location = new Point(493, 234), Size = new Size(85,  26) };
        private Button btnAbout     = new Button { Text = "О программе",  Location = new Point(586, 234), Size = new Size(110, 26) };

        private Label lblFolders    = new Label { Text = "Папки",         Location = new Point(210, 22), AutoSize = true };
        private Label lblFilesList  = new Label { Text = "Файлы",         Location = new Point(210, 232), AutoSize = true };
        private Label lblPath       = new Label { Text = "Путь назначения:", Location = new Point(400, 155), AutoSize = true };

        // Главное меню
        private MenuStrip menu = new MenuStrip();

        private string currentPath = "";

        // ── Конструктор ──────────────────────────────────────────────────
        public Form1()
        {
            Text = "Браузер файлов — Лабораторная работа №7";
            Size = new Size(790, 510);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            MaximizeBox = false;

            BuildMenu();
            Controls.AddRange(new Control[] {
                menu, tvDrives, lbFolders, lbFiles, lblInfo,
                lblPath, txtNewPath, btnUp, btnCreate,
                btnCopy, btnMove, btnRename, btnDelete,
                btnDrives, btnAbout, lblFolders, lblFilesList
            });

            // Обработчики событий
            tvDrives.AfterSelect          += (s, e) => LoadFolder(e.Node.Tag?.ToString() ?? "");
            tvDrives.BeforeExpand         += OnTreeExpand;
            lbFolders.DoubleClick         += (s, e) => { if (lbFolders.SelectedItem != null) LoadFolder(Path.Combine(currentPath, lbFolders.SelectedItem.ToString()!)); };
            lbFiles.SelectedIndexChanged  += ShowFileInfo;
            btnUp.Click                   += (s, e) => { var p = Directory.GetParent(currentPath); if (p != null) LoadFolder(p.FullName); };
            btnCreate.Click               += CreateFolder;
            btnCopy.Click                 += CopyFile;
            btnMove.Click                 += MoveFile;
            btnRename.Click               += RenameFile;
            btnDelete.Click               += DeleteFile;
            btnDrives.Click               += ShowDrivesInfo;
            btnAbout.Click                += (s, e) => ShowAbout();

            LoadDrives();
        }

        // ── Главное меню ─────────────────────────────────────────────────
        private void BuildMenu()
        {
            menu.Dock = DockStyle.None;
            menu.Location = new Point(215, 8);

            var mFile = new ToolStripMenuItem("Файл");
            mFile.DropDownItems.Add("Новая папка",    null, CreateFolder);
            mFile.DropDownItems.Add("Копировать",     null, CopyFile);
            mFile.DropDownItems.Add("Переместить",    null, MoveFile);
            mFile.DropDownItems.Add("Переименовать",  null, RenameFile);
            mFile.DropDownItems.Add("Удалить",        null, DeleteFile);
            mFile.DropDownItems.Add(new ToolStripSeparator());
            mFile.DropDownItems.Add("Выход",          null, (s, e) => Application.Exit());

            var mDrives = new ToolStripMenuItem("Диски");
            mDrives.DropDownItems.Add("Информация о дисках", null, ShowDrivesInfo);

            var mHelp = new ToolStripMenuItem("Справка");
            mHelp.DropDownItems.Add("О программе", null, (s, e) => ShowAbout());

            menu.Items.AddRange(new ToolStripItem[] { mFile, mDrives, mHelp });
        }

        // ── Загрузка дисков в TreeView ───────────────────────────────────
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

        // ── Загрузка содержимого папки ───────────────────────────────────
        private void LoadFolder(string path)
        {
            if (!Directory.Exists(path)) return;
            currentPath = path;
            Text = $"Браузер файлов  —  {path}";
            lbFolders.Items.Clear();
            lbFiles.Items.Clear();
            lblInfo.Text = "";
            txtNewPath.Text = path;

            try {
                foreach (var d in new DirectoryInfo(path).GetDirectories()) lbFolders.Items.Add(d.Name);
                foreach (var f in new DirectoryInfo(path).GetFiles())       lbFiles.Items.Add(f.Name);
            } catch (Exception ex) { MessageBox.Show("Ошибка: " + ex.Message); }
        }

        // ── Информация о выбранном файле ─────────────────────────────────
        private void ShowFileInfo(object? s, EventArgs e)
        {
            if (lbFiles.SelectedItem == null) return;
            try {
                var fi = new FileInfo(Path.Combine(currentPath, lbFiles.SelectedItem.ToString()!));
                lblInfo.Text = $"Имя:      {fi.Name}\n" +
                               $"Размер:   {fi.Length:N0} байт\n" +
                               $"Создан:   {fi.CreationTime:dd.MM.yyyy HH:mm}\n" +
                               $"Изменён:  {fi.LastWriteTime:dd.MM.yyyy HH:mm}\n" +
                               $"Доступ:   {fi.LastAccessTime:dd.MM.yyyy HH:mm}\n" +
                               $"Атрибуты: {fi.Attributes}";
                txtNewPath.Text = fi.FullName;
            } catch (Exception ex) { MessageBox.Show("Ошибка: " + ex.Message); }
        }

        // ── Операции с файлами ───────────────────────────────────────────
        private void CreateFolder(object? s, EventArgs e)
        {
            string name = Prompt("Имя новой папки:", "Создание папки");
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
                File.Move(Path.Combine(currentPath, lbFiles.SelectedItem.ToString()!),
                          Path.Combine(currentPath, newName));
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

        // ── Информация о дисках ──────────────────────────────────────────
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

        // ── Диалог «О программе» ─────────────────────────────────────────
        private void ShowAbout()
        {
            MessageBox.Show(
                "Браузер файлов\n\n" +
                "Лабораторная работа №7\n" +
                "Тема: Работа с файловой системой\n" +
                "Язык: C# / .NET 8 / Windows Forms\n\n" +
                "Возможности:\n" +
                "  • Просмотр дисков, папок и файлов\n" +
                "  • Сведения о файле (размер, даты, атрибуты)\n" +
                "  • Создание, копирование, перемещение,\n" +
                "    переименование и удаление файлов",
                "О программе",
                MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        // ── Вспомогательный диалог ввода ─────────────────────────────────
        private string Prompt(string text, string title, string defaultVal = "")
        {
            var f   = new Form  { Text = title, Size = new Size(380, 130), StartPosition = FormStartPosition.CenterParent, FormBorderStyle = FormBorderStyle.FixedDialog };
            var lbl = new Label { Text = text, Left = 10, Top = 12, AutoSize = true };
            var tb  = new TextBox { Left = 10, Top = 32, Width = 348, Text = defaultVal };
            var ok  = new Button  { Text = "OK",      Left = 190, Top = 62, Size = new Size(75, 26), DialogResult = DialogResult.OK };
            var can = new Button  { Text = "Отмена",  Left = 274, Top = 62, Size = new Size(85, 26), DialogResult = DialogResult.Cancel };
            f.Controls.AddRange(new Control[] { lbl, tb, ok, can });
            f.AcceptButton = ok; f.CancelButton = can;
            return f.ShowDialog() == DialogResult.OK ? tb.Text.Trim() : "";
        }
    }

    // ── Точка входа ──────────────────────────────────────────────────────
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
