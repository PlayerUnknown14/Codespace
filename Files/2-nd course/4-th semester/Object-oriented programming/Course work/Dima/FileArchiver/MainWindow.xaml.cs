using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;
using Microsoft.Win32;
using ModernWpf;

namespace FileArchiver
{
    public partial class MainWindow : Window
    {
        private SmartQueue _smartQueue = new SmartQueue();
        private ArchiveManager _archiveManager = new ArchiveManager();

        public MainWindow()
        {
            InitializeComponent();
            ThemeSelector.SelectedIndex = 0;
        }

        private void ThemeSelector_SelectionChanged(object sender, System.Windows.Controls.SelectionChangedEventArgs e)
        {
            ThemeManager.Current.ApplicationTheme = ThemeSelector.SelectedIndex == 0 ? ApplicationTheme.Light : ApplicationTheme.Dark;
        }

        private void BtnAddFiles_Click(object sender, RoutedEventArgs e)
        {
            OpenFileDialog dlg = new OpenFileDialog { Multiselect = true };
            if (dlg.ShowDialog() == true)
            {
                foreach (string file in dlg.FileNames)
                    if (!FilesList.Items.Contains(file)) FilesList.Items.Add(file);
            }
        }

        private void BtnClearFiles_Click(object sender, RoutedEventArgs e) => FilesList.Items.Clear();

        private async void BtnCompress_Click(object sender, RoutedEventArgs e)
        {
            if (FilesList.Items.Count == 0) return;
            
            string password = PasswordInput.Password;
            string[] files = FilesList.Items.Cast<string>().ToArray();
            string finalArchive = files[0] + ".7z" + (string.IsNullOrEmpty(password) ? "" : ".enc");

            await _smartQueue.EnqueueTaskAsync(async () =>
            {
                StatusText.Text = "Сжатие...";
                QueueStatusText.Text = "ВЫПОЛНЯЕТСЯ";
                QueueStatusText.Foreground = System.Windows.Media.Brushes.Red;

                try {
                    string temp7z = files[0] + ".tmp.7z";
                    await _archiveManager.CompressAsync(files, temp7z);

                    if (!string.IsNullOrEmpty(password)) {
                        StatusText.Text = "Защита Argon2 + AES-256...";
                        await Task.Run(() => CryptoHelper.EncryptFile(temp7z, finalArchive, password));
                        File.Delete(temp7z);
                    } else {
                        File.Move(temp7z, files[0] + ".7z");
                    }
                    StatusText.Text = "Архив успешно создан!";
                }
                catch (Exception ex) { MessageBox.Show(ex.Message); }
            });
            QueueStatusText.Text = "Свободна";
            QueueStatusText.Foreground = System.Windows.Media.Brushes.Green;
        }

        private async void BtnExtract_Click(object sender, RoutedEventArgs e)
        {
            if (FilesList.Items.Count != 1) return;
            string selectedFile = FilesList.Items[0].ToString();
            string password = PasswordInput.Password;
            string outDir = Path.Combine(Path.GetDirectoryName(selectedFile), "Extracted_Files");

            await _smartQueue.EnqueueTaskAsync(async () => {
                try {
                    string toExtract = selectedFile;
                    if (selectedFile.EndsWith(".enc")) {
                        if (string.IsNullOrEmpty(password)) { MessageBox.Show("Нужен пароль!"); return; }
                        StatusText.Text = "Расшифровка...";
                        toExtract = selectedFile + ".tmp.7z";
                        await Task.Run(() => CryptoHelper.DecryptFile(selectedFile, toExtract, password));
                    }
                    
                    Directory.CreateDirectory(outDir);
                    await _archiveManager.ExtractAsync(toExtract, outDir);
                    if (toExtract.Contains(".tmp.7z")) File.Delete(toExtract);
                    StatusText.Text = "Успешно извлечено!";
                } catch (Exception ex) { MessageBox.Show("Ошибка: " + ex.Message); }
            });
        }

        private async void BtnView_Click(object sender, RoutedEventArgs e)
        {
            if (FilesList.Items.Count != 1) return;
            string file = FilesList.Items[0].ToString();
            if (file.EndsWith(".enc")) { MessageBox.Show("Сначала расшифруйте архив."); return; }
            
            try {
                var content = await _archiveManager.GetArchiveContentsAsync(file);
                MessageBox.Show(string.Join("\n", content), "Содержимое архива");
            } catch (Exception ex) { MessageBox.Show(ex.Message); }
        }
    }
}