# Employee Data ETL Script

This Python script reads employee data from an Excel file, transforms the data by adding a new column (`FullName`), and loads the resulting data into a SQL Server database.

## Features

1. **Extract**: Reads employee data from an Excel file.
2. **Transform**: Combines `FirstName` and `LastName` columns to create a new `FullName` column.
3. **Load**: Inserts the transformed data into a SQL Server table named `employee`.

## Prerequisites

- **Python 3.8+**
- **Required Libraries**: Install the following dependencies:
  ```bash
  pip install pandas openpyxl sqlalchemy pyodbc
  ```
- **SQL Server**: A running instance of SQL Server accessible from your environment.

## File Requirements

- **Excel File**: The script expects an Excel file (`employeedata.xlsx`) with the following columns:
  - `FirstName`
  - `LastName`
  
  Place the file in the following location or update the path in the script: (local directory)
  ```
  C:\Users\Desktop\employeedata.xlsx
  ```

## Database Requirements

- The script connects to a SQL Server instance using the following connection string: (local db)
  ```
  mssql://./DESKTOP-CVG0O1Q/datawarehouse?driver=SQL+Server+Native+Client+11.0
  ```
  - Replace `DESKTOP-CVG0O1Q` with your SQL Server instance name.
  - Replace `datawarehouse` with the target database name.
  - Ensure the SQL Server Native Client driver is installed.

- The script attempts to write data to a table named `employee`. If the table does not exist, ensure it is created before running the script.

## Usage

1. **Clone or Download the Script**:  
   Save the script to your working directory.

2. **Run the Script**:  
   Execute the script using Python:
   ```bash
   python script.py
   ```

3. **Verify Data in SQL Server**:  
   Open your SQL Server management tool (e.g., SQL Server Management Studio) and check the `employee` table in the specified database.
