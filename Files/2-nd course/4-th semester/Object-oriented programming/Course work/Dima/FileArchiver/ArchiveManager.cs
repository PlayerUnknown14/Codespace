using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;
using SevenZip;

namespace FileArchiver
{
    public class ArchiveManager
    {
        static ArchiveManager()
        {
            string dllPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "7z.dll");
            SevenZipBase.SetLibraryPath(dllPath);
        }

        public async Task CompressAsync(string[] files, string output)
        {
            await Task.Run(() => {
                var comp = new SevenZipCompressor {
                    ArchiveFormat = OutArchiveFormat.SevenZip,
                    CompressionMethod = CompressionMethod.Lzma2,
                    CompressionLevel = CompressionLevel.Ultra
                };
                comp.CompressFiles(output, files);
            });
        }

        public async Task ExtractAsync(string archive, string folder)
        {
            await Task.Run(() => {
                using var extr = new SevenZipExtractor(archive);
                extr.ExtractArchive(folder);
            });
        }

        public async Task<List<string>> GetArchiveContentsAsync(string path)
        {
            return await Task.Run(() => {
                var list = new List<string>();
                using var extr = new SevenZipExtractor(path);
                foreach (var data in extr.ArchiveFileData)
                    list.Add($"{data.FileName} ({data.Size} bytes)");
                return list;
            });
        }
    }
}