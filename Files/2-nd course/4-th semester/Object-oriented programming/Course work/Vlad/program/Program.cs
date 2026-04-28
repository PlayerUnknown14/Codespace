using EquipmentAccounting.Data;
using EquipmentAccounting.Forms;
using EquipmentAccounting.Models;

namespace EquipmentAccounting;

static class Program
{
    public static User? CurrentUser { get; set; }

    [STAThread]
    static void Main()
    {
        ApplicationConfiguration.Initialize();

        using (var db = new AppDbContext())
        {
            db.Database.EnsureCreated();
        }

        // Показываем форму входа
        var loginForm = new LoginForm();
        if (loginForm.ShowDialog() == DialogResult.OK)
        {
            CurrentUser = loginForm.LoggedInUser;
            Application.Run(new Form1());
        }
    }
}