using EquipmentAccounting.Models;
using Microsoft.EntityFrameworkCore;

namespace EquipmentAccounting.Data;

public class AppDbContext : DbContext
{
    // Таблицы в базе данных
    public DbSet<Equipment> Equipments { get; set; }
    public DbSet<User> Users { get; set; }
    public DbSet<OperationHistory> OperationHistories { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder options)
    {
        // База данных будет храниться в файле equipment.db рядом с .exe
        options.UseSqlite("Data Source=equipment.db");
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Начальные данные — администратор по умолчанию
        modelBuilder.Entity<User>().HasData(new User
        {
            Id = 1,
            Username = "admin",
            // Пароль: admin123
            PasswordHash = "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9",
            Role = "Администратор",
            FullName = "Администратор системы"
        });
    }
}