namespace EquipmentAccounting.Models;

public class Equipment
{
    // Индивидуальный идентификатор в системе
    public int Id { get; set; }
    // Название
    public string Name { get; set; } = "";           
    // Инвентарный номер
    public string InventoryNumber { get; set; } = ""; 
    // Категория
    public string Category { get; set; } = "";        
    // Статус
    public string Status { get; set; } = "В эксплуатации"; 
    // Серийный номер
    public string? SerialNumber { get; set; }         
    public DateTime DateAdded { get; set; } = DateTime.Now;
    // Ответственное лицо
    public string? ResponsiblePerson { get; set; }    
    // Подразделение
    public string? Department { get; set; }           
    // Примечания
    public string? Notes { get; set; }                

    // Навигационное свойство — история операций
    public List<OperationHistory> History { get; set; } = new();
}