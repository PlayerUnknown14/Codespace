namespace EquipmentAccounting.Models;

public class OperationHistory
{
    public int Id { get; set; }
    public int EquipmentId { get; set; }
    public string OperationType { get; set; } = ""; // Добавление / Перемещение / Списание и т.д.
    public string Description { get; set; } = "";
    public DateTime Date { get; set; } = DateTime.Now;
    public string PerformedBy { get; set; } = "";   // Кто выполнил

    // Навигационное свойство
    public Equipment? Equipment { get; set; }
}