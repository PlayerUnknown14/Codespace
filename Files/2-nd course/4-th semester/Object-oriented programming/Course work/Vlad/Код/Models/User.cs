namespace EquipmentAccounting.Models;

public class User
{
    // Индивидуальный идентификатор
    public int Id { get; set; }
    // Логин
    public string Username { get; set; } = "";
    // Пароль в hash-виде
    public string PasswordHash { get; set; } = "";
    // Роль
    public string Role { get; set; } = "Сотрудник";
    // ФИО
    public string FullName { get; set; } = "";
}