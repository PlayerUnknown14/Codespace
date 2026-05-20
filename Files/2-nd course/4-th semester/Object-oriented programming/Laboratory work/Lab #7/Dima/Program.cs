using System;
using System.IO;
using System.Windows.Forms;
using System.Drawing;

namespace FileBrowserApp
{
    public class Form1 : Form
    {
        private ListBox lbFiles = new ListBox { Location = new Point(10, 50), Size = new Size(180, 250) };
        private ListBox lbFolders = new ListBox { Location = new Point(200, 50), Size = new Size(180, 250) };
        private TextBox txtPath = new TextBox { Location = new Point(10, 10), Width = 300 };
        private Button btnGo = new Button { Text = "Отобразить", Location = new Point(320, 8), Size = new Size(80, 25) };
        
        // Кнопки для операций
        private Button btnDelete = new Button { Text = "Удалить", Location = new Point(10, 310), Size = new Size(100, 30) };
        private Button btnCopy = new Button { Text = "Копировать", Location = new Point(120, 310), Size = new Size(100, 30) };
        private Button btnMove = new Button { Text = "Переместить", Location = new Point(230, 310), Size = new Size(100, 30) };
        private TextBox txtNewPath = new TextBox { Location = new Point(10, 350), Width = 380, Text = "Введите новый путь для копии/переноса" };

        private Label lblInfo = new Label { Location = new Point(10, 390), Size = new Size(400, 80) };

        public Form1()
        {
            Text = "Файловый браузер";
            Width = 450; Height = 520;
            Controls.AddRange(new Control[] { lbFiles, lbFolders, txtPath, btnGo, btnDelete, btnCopy, btnMove, txtNewPath, lblInfo });

            btnGo.Click += (s, e) => LoadContent(txtPath.Text);
            btnDelete.Click += DeleteFile;
            btnCopy.Click += CopyFile;
            btnMove.Click += MoveFile;
            lbFiles.SelectedIndexChanged += ShowFileInfo;
        }

        private void LoadContent(string path)
        {
            try {
                DirectoryInfo di = new DirectoryInfo(path);
                txtPath.Text = di.FullName;
                lbFolders.Items.Clear(); lbFiles.Items.Clear();
                foreach (var d in di.GetDirectories()) lbFolders.Items.Add(d.Name);
                foreach (var f in di.GetFiles()) lbFiles.Items.Add(f.Name);
            } catch (Exception ex) { MessageBox.Show("Ошибка: " + ex.Message); }
        }

        private void ShowFileInfo(object sender, EventArgs e)
        {
            if (lbFiles.SelectedItem == null) return;
            FileInfo fi = new FileInfo(Path.Combine(txtPath.Text, lbFiles.SelectedItem.ToString()));
            lblInfo.Text = $"Файл: {fi.Name}\nРазмер: {fi.Length} байт\nСоздан: {fi.CreationTime}";
        }

        private void DeleteFile(object s, EventArgs e) {
            if (lbFiles.SelectedItem == null) return;
            File.Delete(Path.Combine(txtPath.Text, lbFiles.SelectedItem.ToString()));
            LoadContent(txtPath.Text);
        }

private void CopyFile(object s, EventArgs e) 
{
    // Добавили проверку: если путь совпадает с подсказкой или пустой — ничего не делаем
    if (lbFiles.SelectedItem == null || string.IsNullOrWhiteSpace(txtNewPath.Text) || txtNewPath.Text.Contains("Введите новый путь")) 
    {
        MessageBox.Show("Сначала введите корректный путь назначения!");
        return;
    }
    
    try {
        File.Copy(Path.Combine(txtPath.Text, lbFiles.SelectedItem.ToString()), txtNewPath.Text);
        LoadContent(txtPath.Text);
    } catch (Exception ex) { MessageBox.Show("Ошибка: " + ex.Message); }
}
private void MoveFile(object s, EventArgs e) 
{
    // Такая же проверка для перемещения
    if (lbFiles.SelectedItem == null || string.IsNullOrWhiteSpace(txtNewPath.Text) || txtNewPath.Text.Contains("Введите новый путь")) 
    {
        MessageBox.Show("Сначала введите корректный путь назначения!");
        return;
    }
    
    try {
        File.Move(Path.Combine(txtPath.Text, lbFiles.SelectedItem.ToString()), txtNewPath.Text);
        LoadContent(txtPath.Text);
    } catch (Exception ex) { MessageBox.Show("Ошибка: " + ex.Message); }
}

    static class Program {
        [STAThread]
        static void Main() { Application.Run(new Form1()); }
    }
    }
}