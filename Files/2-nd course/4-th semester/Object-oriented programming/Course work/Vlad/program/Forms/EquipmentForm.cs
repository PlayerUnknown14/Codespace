using EquipmentAccounting.Data;
using EquipmentAccounting.Models;

namespace EquipmentAccounting.Forms;

public class EquipmentForm : Form
{
    private readonly Equipment _equipment;
    private readonly bool _isEdit;

    private TextBox txtName, txtInventoryNumber, txtSerialNumber,
                    txtResponsiblePerson, txtDepartment, txtNotes;
    private ComboBox cmbCategory, cmbStatus;
    private Button btnSave, btnCancel;

    public EquipmentForm(Equipment? equipment = null)
    {
        _isEdit = equipment != null;
        _equipment = equipment ?? new Equipment();
        BuildUI();
        if (_isEdit) FillFields();
    }

    private void BuildUI()
    {
        this.Text = _isEdit ? "Редактировать оборудование" : "Добавить оборудование";
        this.Size = new Size(460, 480);
        this.StartPosition = FormStartPosition.CenterParent;
        this.FormBorderStyle = FormBorderStyle.FixedDialog;
        this.MaximizeBox = false;

        int labelX = 20, fieldX = 160, fieldW = 250, rowH = 40, startY = 20;

        Label MakeLabel(string text, int row) => new Label
        {
            Text = text, Left = labelX,
            Top = startY + row * rowH + 5,
            Width = 130, TextAlign = ContentAlignment.MiddleLeft
        };

        TextBox MakeTextBox(int row) => new TextBox
        {
            Left = fieldX, Top = startY + row * rowH,
            Width = fieldW
        };

        // Поля
        var lblName = MakeLabel("Название: *", 0);
        txtName = MakeTextBox(0);

        var lblInv = MakeLabel("Инв. номер: *", 1);
        txtInventoryNumber = MakeTextBox(1);

        var lblCategory = MakeLabel("Категория: *", 2);
        cmbCategory = new ComboBox
        {
            Left = fieldX, Top = startY + 2 * rowH,
            Width = fieldW, DropDownStyle = ComboBoxStyle.DropDownList
        };
        cmbCategory.Items.AddRange(new[]
        {
            "Вычислительная техника", "Периферийные устройства",
            "Сетевое оборудование", "Вспомогательное оснащение", "Прочее"
        });
        cmbCategory.SelectedIndex = 0;

        var lblStatus = MakeLabel("Статус: *", 3);
        cmbStatus = new ComboBox
        {
            Left = fieldX, Top = startY + 3 * rowH,
            Width = fieldW, DropDownStyle = ComboBoxStyle.DropDownList
        };
        cmbStatus.Items.AddRange(new[] { "В эксплуатации", "На обслуживании", "Списано" });
        cmbStatus.SelectedIndex = 0;

        var lblSerial = MakeLabel("Серийный номер:", 4);
        txtSerialNumber = MakeTextBox(4);

        var lblResp = MakeLabel("Ответственный:", 5);
        txtResponsiblePerson = MakeTextBox(5);

        var lblDept = MakeLabel("Подразделение:", 6);
        txtDepartment = MakeTextBox(6);

        var lblNotes = MakeLabel("Примечания:", 7);
        txtNotes = new TextBox
        {
            Left = fieldX, Top = startY + 7 * rowH,
            Width = fieldW, Height = 55, Multiline = true
        };

        btnSave = new Button
        {
            Text = "Сохранить",
            Left = fieldX, Top = startY + 9 * rowH,
            Width = 115, Height = 32,
            BackColor = Color.SeaGreen,
            ForeColor = Color.White,
            FlatStyle = FlatStyle.Flat
        };
        btnSave.Click += BtnSave_Click;

        btnCancel = new Button
        {
            Text = "Отмена",
            Left = fieldX + 125, Top = startY + 9 * rowH,
            Width = 115, Height = 32,
            BackColor = Color.IndianRed,
            ForeColor = Color.White,
            FlatStyle = FlatStyle.Flat
        };
        btnCancel.Click += (s, e) => this.Close();

        this.Controls.AddRange(new Control[]
        {
            lblName, txtName,
            lblInv, txtInventoryNumber,
            lblCategory, cmbCategory,
            lblStatus, cmbStatus,
            lblSerial, txtSerialNumber,
            lblResp, txtResponsiblePerson,
            lblDept, txtDepartment,
            lblNotes, txtNotes,
            btnSave, btnCancel
        });
    }

    private void FillFields()
    {
        txtName.Text = _equipment.Name;
        txtInventoryNumber.Text = _equipment.InventoryNumber;
        txtSerialNumber.Text = _equipment.SerialNumber ?? "";
        txtResponsiblePerson.Text = _equipment.ResponsiblePerson ?? "";
        txtDepartment.Text = _equipment.Department ?? "";
        txtNotes.Text = _equipment.Notes ?? "";

        var catIdx = cmbCategory.Items.IndexOf(_equipment.Category);
        cmbCategory.SelectedIndex = catIdx >= 0 ? catIdx : 0;

        var stIdx = cmbStatus.Items.IndexOf(_equipment.Status);
        cmbStatus.SelectedIndex = stIdx >= 0 ? stIdx : 0;
    }

    private void BtnSave_Click(object? sender, EventArgs e)
    {
        if (string.IsNullOrWhiteSpace(txtName.Text) ||
            string.IsNullOrWhiteSpace(txtInventoryNumber.Text))
        {
            MessageBox.Show("Заполните обязательные поля (*).", "Ошибка",
                MessageBoxButtons.OK, MessageBoxIcon.Warning);
            return;
        }

        _equipment.Name = txtName.Text.Trim();
        _equipment.InventoryNumber = txtInventoryNumber.Text.Trim();
        _equipment.Category = cmbCategory.SelectedItem!.ToString()!;
        _equipment.Status = cmbStatus.SelectedItem!.ToString()!;
        _equipment.SerialNumber = txtSerialNumber.Text.Trim();
        _equipment.ResponsiblePerson = txtResponsiblePerson.Text.Trim();
        _equipment.Department = txtDepartment.Text.Trim();
        _equipment.Notes = txtNotes.Text.Trim();

        using var db = new AppDbContext();

        if (_isEdit)
        {
            db.Equipments.Update(_equipment);
        }
        else
        {
            _equipment.DateAdded = DateTime.Now;
            db.Equipments.Add(_equipment);
        }

        // Сначала сохраняем оборудование — получаем Id
        db.SaveChanges();

        // Теперь Id уже присвоен — записываем историю
        db.OperationHistories.Add(new OperationHistory
        {
            EquipmentId = _equipment.Id,
            OperationType = _isEdit ? "Редактирование" : "Добавление",
            Description = $"{(_isEdit ? "Изменены данные" : "Добавлено оборудование")} «{_equipment.Name}»",
            Date = DateTime.Now,
            PerformedBy = Program.CurrentUser?.FullName ?? "Неизвестно"
        });

        db.SaveChanges();

        this.DialogResult = DialogResult.OK;
        this.Close();
    }
}