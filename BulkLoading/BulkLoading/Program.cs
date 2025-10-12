namespace BulkLoading;

static class Program
{
    /// <summary>
    ///  The main entry point for the application.
    /// </summary>
    [STAThread]
    static void Main()
    {
        // Build configuration
        var configuration = new ConfigurationBuilder()
            .SetBasePath(AppContext.BaseDirectory)
            .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)
            .Build();

        // Setup Dependency Injection
        var services = new ServiceCollection();

        // Register IConfiguration with DI
        services.AddSingleton<IConfiguration>(configuration);

        // Register AppSettings with DI
        services.AddSingleton(configuration.GetSection("AppSettings").Get<AppSettings>());

        // Register MainForm with DI
        services.AddTransient<MainForm>();

        var serviceProvider = services.BuildServiceProvider();

        // Start the application
        Application.SetHighDpiMode(HighDpiMode.SystemAware);
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);

        Application.Run(serviceProvider.GetRequiredService<MainForm>());
    }
}
