using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;
using Konscious.Security.Cryptography;

namespace FileArchiver
{
    public static class CryptoHelper
    {
        // Генерация ключа Argon2
        private static byte[] DeriveKey(string password, byte[] salt)
        {
            using var argon2 = new Argon2id(Encoding.UTF8.GetBytes(password))
            {
                Salt = salt,
                DegreeOfParallelism = 8,
                Iterations = 4,
                MemorySize = 1024 * 64 // 64 MB
            };
            return argon2.GetBytes(32);
        }

        // Шифрование AES-256
        public static void EncryptFile(string input, string output, string password)
        {
            byte[] salt = new byte[16];
            using (var rng = RandomNumberGenerator.Create())
            {
                rng.GetBytes(salt);
            }
            
            byte[] key = DeriveKey(password, salt);

            using Aes aes = Aes.Create();
            aes.Key = key;
            aes.Mode = CipherMode.CBC;
            aes.GenerateIV();

            using FileStream fsOut = new FileStream(output, FileMode.Create);
            fsOut.Write(salt, 0, 16);
            fsOut.Write(aes.IV, 0, 16);

            using CryptoStream cs = new CryptoStream(fsOut, aes.CreateEncryptor(), CryptoStreamMode.Write);
            using FileStream fsIn = new FileStream(input, FileMode.Open);
            fsIn.CopyTo(cs);
        }

        // Дешифрование
        public static void DecryptFile(string input, string output, string password)
        {
            using FileStream fsIn = new FileStream(input, FileMode.Open);
            byte[] salt = new byte[16];
            byte[] iv = new byte[16];
            fsIn.Read(salt, 0, 16);
            fsIn.Read(iv, 0, 16);

            byte[] key = DeriveKey(password, salt);
            using Aes aes = Aes.Create();
            aes.Key = key;
            aes.IV = iv;
            aes.Mode = CipherMode.CBC;

            using CryptoStream cs = new CryptoStream(fsIn, aes.CreateDecryptor(), CryptoStreamMode.Read);
            using FileStream fsOut = new FileStream(output, FileMode.Create);
            cs.CopyTo(fsOut);
        }
    }
}