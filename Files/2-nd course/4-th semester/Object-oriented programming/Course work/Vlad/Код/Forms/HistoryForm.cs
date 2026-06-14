using EquipmentAccounting.Data;
using Microsoft.EntityFrameworkCore;

namespace EquipmentAccounting.Forms;

public class HistoryForm : Form
{
    private DataGridView dgv;
    private Button btnClose;

    public HistoryForm()
    {
        BuildUI();
        LoadHistory();
    }

    private void BuildUI()
    {
        this.Text = "История операций";
        this.Size = new Size(850, 500);
        this.StartPosition = FormStartPosition.CenterParent;

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
            Text = "Закрыть",
            Width = 100, Height = 30,
            Left = 10, Top = 7,
            BackColor = Color.SteelBlue,
            ForeColor = Color.White,
            FlatStyle = FlatStyle.Flat
        };
        btnClose.Click += (s, e) => this.Close();
        panelBottom.Controls.Add(btnClose);

        this.Controls.Add(dgv);
        this.Controls.Add(panelBottom);
    }

    private void LoadHistory()
    {
        using var db = new AppDbContext();
        var history = db.OperationHistories
            .Include(h => h.Equipment)
            .OrderByDescending(h => h.Date)
            .ToList();

        dgv.DataSource = history.Select(h => new
        {
            Дата = h.Date.ToString("dd.MM.yyyy HH:mm"),
            Операция = h.OperationType,
            Оборудование = h.Equipment?.Name ?? "—",
            Описание = h.Description,
            Выполнил = h.PerformedBy
        }).ToList();
    }
}