using EquipmentAccounting.Data;
using EquipmentAccounting.Models;
using EquipmentAccounting.Forms;
using Microsoft.EntityFrameworkCore;
using System.ComponentModel;

namespace EquipmentAccounting;

public partial class Form1 : Form
{
    private DataGridView dgvEquipment;
    private Panel panelTop;
    private Button btnAdd, btnEdit, btnDelete, btnHistory, btnUsers, btnRefresh;
    private TextBox txtSearch;
    private Label lblSearch, lblWelcome;
    private ComboBox cmbStatusFilter;
    private string _sortColumn = "";
    private bool _sortAscending = true;

    public Form1()
    {
        InitializeComponent();
        BuildUI();
        LoadEquipment();
    }

    private void BuildUI()
    {
        this.Text = "Учёт оборудования";
        this.Size = new Size(1100, 650);
        this.StartPosition = FormStartPosition.CenterScreen;

        // Верхняя панель
        panelTop = new Panel
        {
            Dock = DockStyle.Top,
            Height = 55,
            BackColor = Color.SteelBlue,
            Padding = new Padding(10, 10, 10, 0)
        };

        lblWelcome = new Label
        {
            Text = $"Пользователь: {Program.CurrentUser?.FullName}  |  Роль: {Program.CurrentUser?.Role}",
            ForeColor = Color.White,
            Font = new Font("Segoe UI", 10),
            Left = 10, Top = 15, Width = 400
        };

        lblSearch = new Label
        {
            Text = "Поиск:", ForeColor = Color.White,
            Left = 420, Top = 17, Width = 50
        };

        txtSearch = new TextBox { Left = 475, Top = 14, Width = 200 };
        txtSearch.TextChanged += (s, e) => LoadEquipment();

        var lblFilter = new Label
        {
            Text = "Статус:", ForeColor = Color.White,
            Left = 690, Top = 17, Width = 55
        };

        cmbStatusFilter = new ComboBox
        {
            Left = 750, Top = 14, Width = 150,
            DropDownStyle = ComboBoxStyle.DropDownList
        };
        cmbStatusFilter.Items.AddRange(new[] { "Все", "В эксплуатации", "На обслуживании", "Списано" });
        cmbStatusFilter.SelectedIndex = 0;
        cmbStatusFilter.SelectedIndexChanged += (s, e) => LoadEquipment();

        panelTop.Controls.AddRange(new Control[]
        {
            lblWelcome, lblSearch, txtSearch, lblFilter, cmbStatusFilter
        });

        // Панель кнопок
        var panelButtons = new Panel
        {
            Dock = DockStyle.Top,
            Height = 45,
            BackColor = Color.WhiteSmoke,
            Padding = new Padding(5)
        };

        btnAdd = CreateButton("Добавить", Color.SeaGreen, 5);
        btnEdit = CreateButton("Редактировать", Color.SteelBlue, 130);
        btnDelete = CreateButton("Удалить", Color.IndianRed, 285);
        btnHistory = CreateButton("История", Color.SlateGray, 390);
        btnRefresh = CreateButton("Обновить", Color.Gray, 495);

        btnAdd.Click += BtnAdd_Click;
        btnEdit.Click += BtnEdit_Click;
        btnDelete.Click += BtnDelete_Click;
        btnHistory.Click += BtnHistory_Click;
        btnRefresh.Click += (s, e) => LoadEquipment();

        // Кнопка управления пользователями — только для администратора
        if (Program.CurrentUser?.Role == "Администратор")
        {
            btnUsers = CreateButton("Пользователи", Color.DarkSlateBlue, 600);
            btnUsers.Click += (s, e) => new UsersForm().ShowDialog();
            panelButtons.Controls.Add(btnUsers);
        }

        panelButtons.Controls.AddRange(new Control[]
        {
            btnAdd, btnEdit, btnDelete, btnHistory, btnRefresh
        });

        // Таблица оборудования
        dgvEquipment = new DataGridView
        {
            Dock = DockStyle.Fill,
            ReadOnly = true,
            AllowUserToAddRows = false,
            SelectionMode = DataGridViewSelectionMode.FullRowSelect,
            AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill,
            BackgroundColor = Color.White,
            BorderStyle = BorderStyle.None,
            RowHeadersVisible = false,
            Font = new Font("Segoe UI", 9)
        };
        dgvEquipment.ColumnHeadersDefaultCellStyle.BackColor = Color.SteelBlue;
        dgvEquipment.ColumnHeadersDefaultCellStyle.ForeColor = Color.White;
        dgvEquipment.ColumnHeadersDefaultCellStyle.Font = new Font("Segoe UI", 9, FontStyle.Bold);
        dgvEquipment.EnableHeadersVisualStyles = false;
        dgvEquipment.ColumnHeaderMouseClick += DgvEquipment_ColumnHeaderMouseClick;

        this.Controls.Add(dgvEquipment);
        this.Controls.Add(panelButtons);
        this.Controls.Add(panelTop);
    }

    private Button CreateButton(string text, Color color, int left)
    {
        return new Button
        {
            Text = text,
            Left = left, Top = 7,
            Width = 120, Height = 30,
            BackColor = color,
            ForeColor = Color.White,
            FlatStyle = FlatStyle.Flat,
            Font = new Font("Segoe UI", 9)
        };
    }

    private void LoadEquipment()
    {
        using var db = new AppDbContext();
        var query = db.Equipments.AsQueryable();

        // Фильтр по статусу в БД
        if (cmbStatusFilter.SelectedItem?.ToString() != "Все")
            query = query.Where(e => e.Status == cmbStatusFilter.SelectedItem!.ToString());

        // Загружаем в память и сортируем
        var list = query.OrderByDescending(e => e.DateAdded).ToList();

        // Поиск по всем полям (в памяти)
        var search = txtSearch.Text.Trim().ToLower();
        if (!string.IsNullOrEmpty(search))
            list = list.Where(e => SearchInEquipment(e, search)).ToList();

        // Преобразуем в список EquipmentRow
        var rows = list.Select(e => new EquipmentRow
        {
            Id           = e.Id,
            Название     = e.Name,
            Инв_номер    = e.InventoryNumber,
            Категория    = e.Category,
            Статус       = e.Status,
            Ответственный = e.ResponsiblePerson ?? "—",
            Подразделение = e.Department ?? "—",
            Добавлено    = e.DateAdded.ToString("dd.MM.yyyy")
        }).ToList();

        // Применяем сортировку
        rows = SortRows(rows);

        dgvEquipment.DataSource = new BindingList<EquipmentRow>(rows);

        if (dgvEquipment.Columns.Contains("Id"))
            dgvEquipment.Columns["Id"]!.Visible = false;
    }

    private List<EquipmentRow> SortRows(List<EquipmentRow> rows)
    {
        if (string.IsNullOrEmpty(_sortColumn))
            return rows;

        return _sortColumn switch
        {
            "Название" => _sortAscending
                ? rows.OrderBy(r => r.Название).ToList()
                : rows.OrderByDescending(r => r.Название).ToList(),
            "Инв_номер" => _sortAscending
                ? rows.OrderBy(r => r.Инв_номер).ToList()
                : rows.OrderByDescending(r => r.Инв_номер).ToList(),
            "Категория" => _sortAscending
                ? rows.OrderBy(r => r.Категория).ToList()
                : rows.OrderByDescending(r => r.Категория).ToList(),
            "Статус" => _sortAscending
                ? rows.OrderBy(r => r.Статус).ToList()
                : rows.OrderByDescending(r => r.Статус).ToList(),
            "Ответственный" => _sortAscending
                ? rows.OrderBy(r => r.Ответственный).ToList()
                : rows.OrderByDescending(r => r.Ответственный).ToList(),
            "Подразделение" => _sortAscending
                ? rows.OrderBy(r => r.Подразделение).ToList()
                : rows.OrderByDescending(r => r.Подразделение).ToList(),
            "Добавлено" => _sortAscending
                ? rows.OrderBy(r => r.Добавлено).ToList()
                : rows.OrderByDescending(r => r.Добавлено).ToList(),
            _ => rows
        };
    }

    private bool SearchInEquipment(Equipment e, string searchLower)
    {
        return ContainsSearch(e.Name, searchLower) ||
            ContainsSearch(e.InventoryNumber, searchLower) ||
            ContainsSearch(e.Category, searchLower) ||
            ContainsSearch(e.Status, searchLower) ||
            ContainsSearch(e.SerialNumber, searchLower) ||
            ContainsSearch(e.ResponsiblePerson, searchLower) ||
            ContainsSearch(e.Department, searchLower) ||
            ContainsSearch(e.Notes, searchLower) ||
            ContainsSearch(e.Id.ToString(), searchLower);
    }

    private bool ContainsSearch(string? value, string search)
        => !string.IsNullOrEmpty(value) && value.ToLower().Contains(search);

    private Equipment? GetSelectedEquipment()
    {
        if (dgvEquipment.CurrentRow == null) return null;
        var id = (int)dgvEquipment.CurrentRow.Cells["Id"].Value;
        using var db = new AppDbContext();
        return db.Equipments.Find(id);
    }

    private void BtnAdd_Click(object? sender, EventArgs e)
    {
        var form = new EquipmentForm();
        if (form.ShowDialog() == DialogResult.OK)
            LoadEquipment();
    }

    private void BtnEdit_Click(object? sender, EventArgs e)
    {
        var eq = GetSelectedEquipment();
        if (eq == null) { MessageBox.Show("Выберите оборудование."); return; }

        var form = new EquipmentForm(eq);
        if (form.ShowDialog() == DialogResult.OK)
            LoadEquipment();
    }

    private void BtnDelete_Click(object? sender, EventArgs e)
    {
        var eq = GetSelectedEquipment();
        if (eq == null) { MessageBox.Show("Выберите оборудование."); return; }

        if (Program.CurrentUser?.Role != "Администратор")
        {
            MessageBox.Show("Недостаточно прав.", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            return;
        }

        var confirm = MessageBox.Show($"Удалить «{eq.Name}»?", "Подтверждение",
            MessageBoxButtons.YesNo, MessageBoxIcon.Question);

        if (confirm == DialogResult.Yes)
        {
            using var db = new AppDbContext();
            db.Equipments.Remove(db.Equipments.Find(eq.Id)!);
            db.SaveChanges();
            LoadEquipment();
        }
    }

    private void BtnHistory_Click(object? sender, EventArgs e)
    {
        new HistoryForm().ShowDialog();
    }

    private void DgvEquipment_ColumnHeaderMouseClick(object? sender, DataGridViewCellMouseEventArgs e)
    {
        var columnName = dgvEquipment.Columns[e.ColumnIndex].Name;
        if (columnName == "Id") return;

        // Если кликнули на ту же колонку, меняем направление сортировки
        if (_sortColumn == columnName)
            _sortAscending = !_sortAscending;
        else
        {
            _sortColumn = columnName;
            _sortAscending = true;
        }

        LoadEquipment();
    }
}

public class EquipmentRow
{
    public int Id { get; set; }
    public string Название { get; set; } = "";
    public string Инв_номер { get; set; } = "";
    public string Категория { get; set; } = "";
    public string Статус { get; set; } = "";
    public string Ответственный { get; set; } = "";
    public string Подразделение { get; set; } = "";
    public string Добавлено { get; set; } = "";
}