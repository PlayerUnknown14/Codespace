using EquipmentAccounting.Models;
using Microsoft.EntityFrameworkCore;

namespace EquipmentAccounting.Data;

public class AppDbContext : DbContext
{
    // Таблица оборудования
    public DbSet<Equipment> Equipments { get; set; }
    // Таблица юзеров
    public DbSet<User> Users { get; set; }
    // Таблица истории действий
    public DbSet<OperationHistory> OperationHistories { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder options)
    {
        // База данных будет храниться в файле equipment.db
        options.UseSqlite("Data Source=equipment.db");
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Создание начальных данных для админа по умолчанию
        modelBuilder.Entity<User>().HasData(new User
        {
            Id = 1,
            Username = "admin",
            // Пароль: admin123
            PasswordHash = "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9",
            Role = "Администратор",
            FullName = "Гордов В.Т."
        });
    }
}