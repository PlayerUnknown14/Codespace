namespace EquipmentAccounting.Models;

public class User
{
    public int Id { get; set; }
    public string Username { get; set; } = "";
    public string PasswordHash { get; set; } = "";
    public string Role { get; set; } = "Сотрудник"; // Администратор / Менеджер / Сотрудник
    public string FullName { get; set; } = "";
}