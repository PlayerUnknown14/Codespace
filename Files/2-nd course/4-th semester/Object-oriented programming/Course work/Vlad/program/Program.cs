using EquipmentAccounting.Data;
using EquipmentAccounting.Forms;
using EquipmentAccounting.Models;

namespace EquipmentAccounting;

static class Program
{
    /// <summary>
    /// Хранит текущего вошедшего пользователя
    /// /// </summary>
    public static User? CurrentUser { get; set; }

    [STAThread]
    static void Main()
    {
        // Настройка DPI и стилей Windows
        ApplicationConfiguration.Initialize();

        // Создаём БД при первом запуске
        using (var db = new AppDbContext())
        {
            db.Database.EnsureCreated();
        }

        // Первое окно - форма ввода
        var loginForm = new LoginForm();
        if (loginForm.ShowDialog() == DialogResult.OK)
        {
            CurrentUser = loginForm.LoggedInUser;
            Application.Run(new Form1()); // Юзер вошёл - открываем главное меню
        }
    }
}