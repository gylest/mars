namespace BulkLoading;

public partial class MainForm : Form
{
    private readonly AppSettings _appSettings;
    private readonly string _connectionString;

    public MainForm(AppSettings appSettings, IConfiguration configuration)
    {
        _appSettings = appSettings;
        _connectionString = configuration.GetConnectionString("PrimaryConnectionSQL");

        InitializeComponent();
    }

    private static void MakeData(System.Data.DataTable tablex, int rowCount)
    {
        // Declare variables for DataColumn and DataRow objects.
        DataColumn column;
        DataRow row;

        // Create new DataColumn, set DataType, 
        // ColumnName and add to DataTable.    
        column = new DataColumn
        {
            DataType = System.Type.GetType("System.Int32"),
            ColumnName = "id",
            ReadOnly = true,
            Unique = true
        };
        // Add the Column to the DataColumnCollection.
        tablex.Columns.Add(column);

        // Create second column.
        column = new DataColumn
        {
            DataType = System.Type.GetType("System.String"),
            ColumnName = "Name",
            AutoIncrement = false,
            ReadOnly = false,
            Unique = false
        };
        // Add the column to the table.
        tablex.Columns.Add(column);

        // Create second column.
        column = new DataColumn
        {
            DataType = System.Type.GetType("System.String"),
            ColumnName = "Address",
            AutoIncrement = false,
            ReadOnly = false,
            Unique = false
        };
        // Add the column to the table.
        tablex.Columns.Add(column);

        for (int i = 0; i < rowCount; i++)
        {
            row = tablex.NewRow();
            row["id"] = i;
            row["Name"] = "Tony Gyles " + i;
            row["Address"] = "Turnberry Drive " + i;
            tablex.Rows.Add(row);
        }
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
        int MAXROWS = _appSettings.MaxRows;
        DateTime begintm = DateTime.Now;

        try
        {
            using (DataTable table = new DataTable("MyTableRow"))
            {
                MakeData(table, MAXROWS);

                using (SqlConnection connection = new SqlConnection(this._connectionString))
                {
                    connection.Open();

                    using (SqlCommand cmd = new SqlCommand())
                    {
                        cmd.Connection = connection;
                        cmd.CommandType = CommandType.Text;

                        // Create parameterized query
                        string sqlCommand = $"Insert into [BulkLoading].[Contact] (id, Name, Address) values ( @Id, @Name, @Address)";

                        // Use parameters to provide the data values
                        for (int i = 0; i < MAXROWS; i++)
                        {
                            cmd.Parameters.Clear();

                            cmd.Parameters.AddWithValue("@Id", table.Rows[i]["id"]);
                            cmd.Parameters.AddWithValue("@Name", table.Rows[i]["Name"]);
                            cmd.Parameters.AddWithValue("@Address", table.Rows[i]["Address"]);

                            cmd.CommandText = sqlCommand;
                            cmd.ExecuteNonQuery();
                        }
                    }
                }
            }

            DateTime endtm = DateTime.Now;
            TimeSpan Duration = endtm - begintm;

            this.txtRowElapsed.Text = Duration.Seconds.ToString(CultureInfo.CurrentCulture);
        }
        catch (Exception exc)
        {
            Debug.WriteLine($"Exception during RowBy. Message = {exc.Message}");
            ShowError(exc);
        }
    }

    private void btnBulk_Click(object sender, EventArgs e)
    {
        int MAXROWS = _appSettings.MaxRows;
        DateTime begintm = DateTime.Now;

        try
        {
            using (DataTable bulkTable = new DataTable("MyTableBulk"))
            {
                MakeData(bulkTable, MAXROWS);

                using (SqlConnection connection = new SqlConnection(this._connectionString))
                {
                    connection.Open();

                    using (SqlBulkCopy bulkCopy = new SqlBulkCopy(connection))
                    {
                        bulkCopy.DestinationTableName = "[BulkLoading].[Contact]";

                        // Write from the source to the destination.
                        bulkCopy.WriteToServer(bulkTable);
                    }

                }
            }

            DateTime endtm = DateTime.Now;
            TimeSpan Duration = endtm - begintm;

            this.txtBulkElapsed.Text = Duration.Seconds.ToString(CultureInfo.CurrentCulture);
        }
        catch (Exception exc)
        {
            Debug.WriteLine($"Exception during Bulk Copy. Message = {exc.Message}");
            ShowError(exc);
        }
    }


    //
    // Create target table if it does not exist
    //
    private void CreateTable()
    {
        try
        {
            using (SqlConnection con = new SqlConnection(this._connectionString))
            {
                con.Open();

                DataTable dTable  = con.GetSchema("TABLES", new string[] { null, null, "Contact" });

                if (dTable.Rows.Count == 0)
                {
                    string query = $"CREATE SCHEMA [BulkLoading]";

                    using (SqlCommand cmd = new SqlCommand(query, con))
                    {
                        cmd.ExecuteNonQuery();
                        Debug.WriteLine("Schema Created Successfully");
                    }
                }

                if (dTable.Rows.Count == 0)
                {
                    string query = $"CREATE TABLE [BulkLoading].[Contact]([id] [int] NOT NULL,[Name] [nvarchar](50) NOT NULL,[Address] [nvarchar](50) NULL,[Date] datetime2 DEFAULT GETDATE()) ON [PRIMARY]";

                    using (SqlCommand cmd = new SqlCommand(query, con))
                    {
                        cmd.ExecuteNonQuery();
                        Debug.WriteLine("Table Created Successfully");
                    }
                }
            }

        }
        catch (Exception ex)
        {
            Debug.WriteLine($"Exception during Schema/Table Creation. Message = {ex.Message}");
            throw;
        }
    }

    private void btnCreate_Click(object sender, EventArgs e)
    {
        try
        {
            CreateTable();
        }
        catch (Exception exc)
        {
            ShowError(exc);
        }
    }
}
