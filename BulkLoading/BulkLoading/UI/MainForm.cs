namespace BulkLoading.UI;

public partial class MainForm : Form
{
    private readonly AppSettings _appSettings;
    private readonly ManageDatabase _manageDatabase;

    public MainForm(AppSettings appSettings, IConfiguration configuration)
    {
        _appSettings = appSettings;
        string connectionString = configuration.GetConnectionString("PrimaryConnectionSQL");
        _manageDatabase = new ManageDatabase(connectionString, _appSettings.MaxRows);

        InitializeComponent();
    }

    private static void ShowError(Exception exc, string caption = "Error")
    {
        string messageBoxText = exc.Message;
        MessageBoxButtons button = MessageBoxButtons.OK;
        MessageBoxIcon icon = MessageBoxIcon.Error;

        MessageBox.Show(messageBoxText, caption, button, icon);
    }

    private void btnRowBy_Click(object sender, EventArgs e)
    {
        try
        {
           TimeSpan duration = _manageDatabase.ProcessRowByRow();

           txtRowElapsed.Text = duration.TotalSeconds.ToString("F4",CultureInfo.CurrentCulture);

        }
        catch (Exception exc)
        {
            Debug.WriteLine($"Exception during RowBy. Message = {exc.Message}");
            ShowError(exc);
        }
    }

    private void btnBulk_Click(object sender, EventArgs e)
    {
        try
        {
            TimeSpan duration = _manageDatabase.ProcessBulk();

            txtBulkElapsed.Text = duration.TotalSeconds.ToString("F4", CultureInfo.CurrentCulture);
        }
        catch (Exception exc)
        {
            Debug.WriteLine($"Exception during Bulk Copy. Message = {exc.Message}");
            ShowError(exc);
        }
    }

    private void btnCreate_Click(object sender, EventArgs e)
    {
        try
        {
            _manageDatabase.CreateTable();
        }
        catch (Exception exc)
        {
            ShowError(exc);
        }
    }
}
