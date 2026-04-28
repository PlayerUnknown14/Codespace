using System.Security.Cryptography;
using System.Text;

namespace EquipmentAccounting.Services;

public static class PasswordHelper
{
    public static string Hash(string password)
    {
        var bytes = SHA256.HashData(Encoding.UTF8.GetBytes(password));
        return Convert.ToHexString(bytes).ToLower();
    }

    public static bool Verify(string password, string hash)
    {
        return Hash(password) == hash;
    }
}