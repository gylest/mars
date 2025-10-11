using System;
using Microsoft.Extensions.Configuration;

namespace BulkLoading
{
    public class AppSettings
    {
        public int? MaxRows { get; set; } = 1000;
    }
}
