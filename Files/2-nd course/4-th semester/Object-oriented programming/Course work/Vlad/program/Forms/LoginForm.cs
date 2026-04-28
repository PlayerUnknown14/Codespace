using EquipmentAccounting.Data;
using EquipmentAccounting.Models;
using EquipmentAccounting.Services;

namespace EquipmentAccounting.Forms;

public class LoginForm : Form
{
    private Label lblTitle, lblUsername, lblPassword;
    private TextBox txtUsername, txtPassword;
    private Button btnLogin;

    public User? LoggedInUser { get; private set; }

    public LoginForm()
    {
        InitializeComponents();
    }

    private void InitializeComponents()
    {
        this.Text = "Учёт оборудования — Вход";
        this.Size = new Size(380, 280);
        this.StartPosition = FormStartPosition.CenterScreen;
        this.FormBorderStyle = FormBorderStyle.FixedDialog;
        this.MaximizeBox = false;

        lblTitle = new Label
        {
            Text = "Вход в систему",
            Font = new Font("Segoe UI", 14, FontStyle.Bold),
            TextAlign = ContentAlignment.MiddleCenter,
            Dock = DockStyle.Top,
            Height = 60
        };

        lblUsername = new Label { Text = "Логин:", Left = 40, Top = 80, Width = 80 };
        txtUsername = new TextBox { Left = 130, Top = 77, Width = 200 };

        lblPassword = new Label { Text = "Пароль:", Left = 40, Top = 120, Width = 80 };
        txtPassword = new TextBox { Left = 130, Top = 117, Width = 200, PasswordChar = '*' };

        btnLogin = new Button
        {
            Text = "Войти",
            Left = 130, Top = 165,
            Width = 200, Height = 35,
            BackColor = Color.SteelBlue,
            ForeColor = Color.White,
            FlatStyle = FlatStyle.Flat
        };
        btnLogin.Click += BtnLogin_Click;

        // Нажатие Enter вместо кнопки
        this.AcceptButton = btnLogin;

        this.Controls.AddRange(new Control[]
        {
            lblTitle, lblUsername, txtUsername,
            lblPassword, txtPassword, btnLogin
        });
    }

    private void BtnLogin_Click(object? sender, EventArgs e)
    {
        var username = txtUsername.Text.Trim();
        var password = txtPassword.Text;

        if (string.IsNullOrEmpty(username) || string.IsNullOrEmpty(password))
        {
            MessageBox.Show("Заполните все поля.", "Ошибка",
                MessageBoxButtons.OK, MessageBoxIcon.Warning);
            return;
        }

        using var db = new AppDbContext();
        var user = db.Users.FirstOrDefault(u => u.Username == username);

        if (user == null)
        {
            MessageBox.Show("Пользователь не найден.", "Ошибка",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
            return;
        }

        if (!PasswordHelper.Verify(password, user.PasswordHash))
        {
            MessageBox.Show("Неверный пароль.", "Ошибка",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
            return;
        }

        LoggedInUser = user;
        this.DialogResult = DialogResult.OK;
        this.Close();
    }
}