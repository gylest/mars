namespace BulkLoading.Services;

public class ManageDatabase
{
    private readonly string _connectionString;
    private readonly int _maxRows;

    public ManageDatabase(string connectionString, int maxRows)
    {
        _connectionString = connectionString;
        _maxRows = maxRows;
    }

    private static void MakeData(DataTable tablex, int rowCount)
    {
        // Declare variables for DataColumn and DataRow objects.
        DataColumn column;
        DataRow row;

        // Create first column
        column = new DataColumn
        {
            DataType = Type.GetType("System.Int32"),
            ColumnName = "id",
            ReadOnly = true,
            Unique = true
        };
        // Add the Column to the DataColumnCollection.
        tablex.Columns.Add(column);

        // Create second column
        column = new DataColumn
        {
            DataType = Type.GetType("System.String"),
            ColumnName = "Name",
            AutoIncrement = false,
            ReadOnly = false,
            Unique = false
        };
        // Add the column to the table.
        tablex.Columns.Add(column);

        // Create third column
        column = new DataColumn
        {
            DataType = Type.GetType("System.String"),
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

    //
    // Create target table if it does not exist
    //
    public void CreateTable()
    {
        using (SqlConnection con = new SqlConnection(_connectionString))
        {
            con.Open();

            DataTable dTable = con.GetSchema("TABLES", new string[] { null, null, "Contact" });

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

    public TimeSpan ProcessRowByRow()
    {
        DateTime beginTime = DateTime.Now;

        using (DataTable table = new DataTable("MyTableRow"))
        {
            MakeData(table, _maxRows);

            using (SqlConnection connection = new SqlConnection(_connectionString))
            {
                connection.Open();

                using (SqlCommand cmd = new SqlCommand())
                {
                    cmd.Connection = connection;
                    cmd.CommandType = CommandType.Text;

                    // Create parameterized query
                    string sqlCommand = $"Insert into [BulkLoading].[Contact] (id, Name, Address) values ( @Id, @Name, @Address)";

                    // Use parameters to provide the data values
                    for (int i = 0; i < _maxRows; i++)
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

        DateTime endTime = DateTime.Now;
        TimeSpan duration = endTime - beginTime;

        return duration;

    }

    public TimeSpan ProcessBulk()
    {
        DateTime beginTime = DateTime.Now;

        using (DataTable bulkTable = new DataTable("MyTableBulk"))
        {
            MakeData(bulkTable, _maxRows);

            using (SqlConnection connection = new SqlConnection(_connectionString))
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

        DateTime endTime = DateTime.Now;
        TimeSpan duration = endTime - beginTime;

        return duration;
    }
}
