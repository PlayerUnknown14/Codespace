namespace EquipmentAccounting.Models;

public class Equipment
{
    public int Id { get; set; }
    public string Name { get; set; } = "";           // Название
    public string InventoryNumber { get; set; } = ""; // Инвентарный номер
    public string Category { get; set; } = "";        // Категория
    public string Status { get; set; } = "В эксплуатации"; // Статус
    public string? SerialNumber { get; set; }         // Серийный номер
    public DateTime DateAdded { get; set; } = DateTime.Now;
    public string? ResponsiblePerson { get; set; }    // Ответственное лицо
    public string? Department { get; set; }           // Подразделение
    public string? Notes { get; set; }                // Примечания

    // Навигационное свойство — история операций
    public List<OperationHistory> History { get; set; } = new();
}