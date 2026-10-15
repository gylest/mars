# BulkLoading

A Windows Forms application to compare SQL Server performance for inserting rows using two methods:  
- **Row by Row** (individual `INSERT` statements)  
- **Bulk Insert** (using `SqlBulkCopy`)  

## Overview

BulkLoading demonstrates the performance difference between inserting data into a SQL Server database one row at a time versus using bulk operations. This is useful for understanding and benchmarking data loading strategies in .NET applications.

## Features

- Generate sample data in-memory
- Insert data row-by-row using parameterized SQL commands
- Insert data in bulk using `SqlBulkCopy`
- Measure and display elapsed time for each method
- Create the target table and schema if they do not exist

## Prerequisites

- .NET 10 SDK
- SQL Server instance accessible from your machine

## NugGet Packages

The NuGet packages used by this project are specified in the file `nuget.config`.

This file has environment variables to support my private NuGet source in GitHub:

| Item                | Description                               |
|---------------------|-------------------------------------------|
| GH_USERNAME         | GitHub username                           |
| GH_TOKEN            | GitHub personal access token              |

The GitHub token has an expiry and needs to be either renewed or replaced with a new token. The token must have the `read:packages` scope to access private NuGet packages.

In actual fact , none of the private packages in GitHub are actually used in this project , but the configuration is left in place for demonstration purposes.

## Managing Environment Variables using PowerShell

To set environment variables:-

[System.Environment]::SetEnvironmentVariable('GH_USERNAME', 'xxx', 'User')
[System.Environment]::SetEnvironmentVariable('GH_TOKEN', 'yyy', 'User')

To read these variables:-

Get-ChildItem Env:

## Configuration Data

Configuration data is stored in `appsettings.json`.  

| Item                | Description                               |
|---------------------|-------------------------------------------|
| PrimaryConnectionSQL| Connection string for the primary database|
| MaxRows             | Maximum number of rows to process         |

## How to Run

1. Build the solution in Visual Studio 2026 or with the .NET CLI.
2. Run the application:
   - From Visual Studio: Press `F5` or select `Start`.
   - From command line:  
     ```
     dotnet run --project BulkLoading
     ```
   - Or run the built executable:
     ```
     .\BulkLoading.exe
     ```

## Usage

1. Click **Create Table** to create the required schema and table in your database.
2. Click **Row by Row** to insert data one row at a time and see the elapsed time.
3. Click **Bulk** to insert data using bulk copy and compare the elapsed time.

## License

This project is for demonstration and educational purposes.

