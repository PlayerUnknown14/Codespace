using System;
using System.Threading;
using System.Threading.Tasks;

namespace FileArchiver
{
    public class SmartQueue
    {
        private readonly SemaphoreSlim _semaphore = new SemaphoreSlim(1, 1);

        public async Task EnqueueTaskAsync(Func<Task> task)
        {
            await _semaphore.WaitAsync();
            try { await task(); }
            finally { _semaphore.Release(); }
        }
    }
}