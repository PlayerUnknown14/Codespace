namespace EquipmentAccounting.Models;

/// <summary>
/// Класс для хранения истории операций с оборудованием
/// </summary>
public class OperationHistory
{
    // Уникальный идентификатор лога
    public int Id { get; set; }
    // Идентификатор оборудования, с которым связана операция
    public int EquipmentId { get; set; }
    // Тип операции
    public string OperationType { get; set; } = ""; 
    // Подробное описание
    public string Description { get; set; } = "";
    // Дата и время выполнения
    public DateTime Date { get; set; } = DateTime.Now;
    // Кто выполнил
    public string PerformedBy { get; set; } = "";   

    // Навигационное свойство
    public Equipment? Equipment { get; set; }
}