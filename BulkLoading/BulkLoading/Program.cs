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
        services.AddSingleton<IConfiguration>(configuration);

        // Bind AppSettings section to strongly typed class
        var appSettings = new AppSettings();
        configuration.GetSection("AppSettings").Bind(appSettings);
        services.AddSingleton(appSettings);

        services.AddTransient<MainForm>();

        var serviceProvider = services.BuildServiceProvider();

        // Start the application
        Application.SetHighDpiMode(HighDpiMode.SystemAware);
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);

        Application.Run(serviceProvider.GetRequiredService<MainForm>());
    }
}
