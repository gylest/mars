using System;
using Microsoft.Extensions.Configuration;

namespace BulkLoading
{
    public static class AppSettings
    {
        private static IConfigurationRoot? _config;
        public static IConfiguration Configuration => _config ??= Build();
        public static string? PrimaryConnection => Configuration.GetConnectionString("PrimaryConnectionSQL");
        public static int? MaxRows => Configuration.GetSection("AppSettings").GetValue<int?>("MaxRows");
        private static IConfigurationRoot Build() =>
            new ConfigurationBuilder()
                .SetBasePath(AppContext.BaseDirectory)
                .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)
                .AddEnvironmentVariables()
                .Build();
    }
}
