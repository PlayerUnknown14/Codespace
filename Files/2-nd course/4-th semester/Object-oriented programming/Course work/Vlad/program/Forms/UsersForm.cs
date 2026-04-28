using EquipmentAccounting.Data;
using EquipmentAccounting.Models;
using EquipmentAccounting.Services;

namespace EquipmentAccounting.Forms;

public class UsersForm : Form
{
    private DataGridView dgv;
    private Button btnAdd, btnDelete, btnClose;

    public UsersForm()
    {
        BuildUI();
        LoadUsers();
    }

    private void BuildUI()
    {
        this.Text = "Управление пользователями";
        this.Size = new Size(700, 450);
        this.StartPosition = FormStartPosition.CenterParent;

        var panelTop = new Panel { Dock = DockStyle.Top, Height = 45, BackColor = Color.WhiteSmoke };

        btnAdd = new Button
        {
            Text = "+ Добавить", Left = 10, Top = 8, Width = 110, Height = 30,
            BackColor = Color.SeaGreen, ForeColor = Color.White, FlatStyle = FlatStyle.Flat
        };
        btnAdd.Click += BtnAdd_Click;

        btnDelete = new Button
        {
            Text = "Удалить", Left = 130, Top = 8, Width = 100, Height = 30,
            BackColor = Color.IndianRed, ForeColor = Color.White, FlatStyle = FlatStyle.Flat
        };
        btnDelete.Click += BtnDelete_Click;

        panelTop.Controls.AddRange(new Control[] { btnAdd, btnDelete });

        dgv = new DataGridView
        {
            Dock = DockStyle.Fill,
            ReadOnly = true,
            AllowUserToAddRows = false,
            SelectionMode = DataGridViewSelectionMode.FullRowSelect,
            AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill,
            RowHeadersVisible = false,
            BackgroundColor = Color.White,
            Font = new Font("Segoe UI", 9)
        };
        dgv.ColumnHeadersDefaultCellStyle.BackColor = Color.SteelBlue;
        dgv.ColumnHeadersDefaultCellStyle.ForeColor = Color.White;
        dgv.ColumnHeadersDefaultCellStyle.Font = new Font("Segoe UI", 9, FontStyle.Bold);
        dgv.EnableHeadersVisualStyles = false;

        var panelBottom = new Panel { Dock = DockStyle.Bottom, Height = 45 };
        btnClose = new Button
        {
            Text = "Закрыть", Left = 10, Top = 7, Width = 100, Height = 30,
            BackColor = Color.SteelBlue, ForeColor = Color.White, FlatStyle = FlatStyle.Flat
        };
        btnClose.Click += (s, e) => this.Close();
        panelBottom.Controls.Add(btnClose);

        this.Controls.Add(dgv);
        this.Controls.Add(panelTop);
        this.Controls.Add(panelBottom);
    }

    private void LoadUsers()
    {
        using var db = new AppDbContext();
        var users = db.Users.ToList();
        dgv.DataSource = users.Select(u => new
        {
            u.Id,
            Логин = u.Username,
            ФИО = u.FullName,
            Роль = u.Role
        }).ToList();

        if (dgv.Columns.Contains("Id"))
            dgv.Columns["Id"]!.Visible = false;
    }

    private void BtnAdd_Click(object? sender, EventArgs e)
    {
        // Простой диалог добавления пользователя
        var dialog = new Form
        {
            Text = "Новый пользователь",
            Size = new Size(360, 280),
            StartPosition = FormStartPosition.CenterParent,
            FormBorderStyle = FormBorderStyle.FixedDialog,
            MaximizeBox = false
        };

        var fields = new (Label lbl, Control ctrl)[]
        {
            (new Label { Text = "Логин:", Left = 20, Top = 25, Width = 100 },
            new TextBox { Left = 130, Top = 22, Width = 180 }),
            (new Label { Text = "Пароль:", Left = 20, Top = 65, Width = 100 },
            new TextBox { Left = 130, Top = 62, Width = 180, PasswordChar = '*' }),
            (new Label { Text = "ФИО:", Left = 20, Top = 105, Width = 100 },
            new TextBox { Left = 130, Top = 102, Width = 180 }),
            (new Label { Text = "Роль:", Left = 20, Top = 145, Width = 100 },
            new ComboBox
            {
                Left = 130, Top = 142, Width = 180,
                DropDownStyle = ComboBoxStyle.DropDownList,
                Items = { "Сотрудник", "Менеджер", "Администратор" },
                SelectedIndex = 0
            })
        };

        var btnSave = new Button
        {
            Text = "Сохранить", Left = 130, Top = 190,
            Width = 110, Height = 30,
            BackColor = Color.SeaGreen, ForeColor = Color.White, FlatStyle = FlatStyle.Flat
        };

        btnSave.Click += (s, e) =>
        {
            var login = ((TextBox)fields[0].ctrl).Text.Trim();
            var pass = ((TextBox)fields[1].ctrl).Text;
            var fullName = ((TextBox)fields[2].ctrl).Text.Trim();
            var role = ((ComboBox)fields[3].ctrl).SelectedItem!.ToString()!;

            if (string.IsNullOrEmpty(login) || string.IsNullOrEmpty(pass) || string.IsNullOrEmpty(fullName))
            {
                MessageBox.Show("Заполните все поля.", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            using var db = new AppDbContext();
            db.Users.Add(new User
            {
                Username = login,
                PasswordHash = PasswordHelper.Hash(pass),
                FullName = fullName,
                Role = role
            });
            db.SaveChanges();
            dialog.DialogResult = DialogResult.OK;
            dialog.Close();
        };

        foreach (var (lbl, ctrl) in fields)
            dialog.Controls.AddRange(new Control[] { lbl, ctrl });
        dialog.Controls.Add(btnSave);

        if (dialog.ShowDialog() == DialogResult.OK)
            LoadUsers();
    }

    private void BtnDelete_Click(object? sender, EventArgs e)
    {
        if (dgv.CurrentRow == null) return;
        var id = (int)dgv.CurrentRow.Cells["Id"].Value;

        if (id == Program.CurrentUser?.Id)
        {
            MessageBox.Show("Нельзя удалить текущего пользователя.", "Ошибка",
                MessageBoxButtons.OK, MessageBoxIcon.Warning);
            return;
        }

        if (MessageBox.Show("Удалить пользователя?", "Подтверждение",
            MessageBoxButtons.YesNo) == DialogResult.Yes)
        {
            using var db = new AppDbContext();
            var user = db.Users.Find(id);
            if (user != null) { db.Users.Remove(user); db.SaveChanges(); }
            LoadUsers();
        }
    }
}