import sqlite3

# Создание подключения и курсора
with sqlite3.connect('person.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Departments (
        DepartmentID INTEGER PRIMARY KEY,
        DepartmentName TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
        EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT,
        LastName TEXT,
        DepartmentID INTEGER,
        FOREIGN KEY(DepartmentID) REFERENCES Departments(DepartmentID))''')

    cursor.execute('DELETE FROM Departments')

    cursor.execute('''INSERT INTO Departments (DepartmentID, DepartmentName)
    VALUES
    (101, "HR"), (102, "IT"), (103, "Sales")''')

    cursor.execute('DELETE FROM Employees')

    cursor.execute('''INSERT INTO Employees (FirstName, LastName, DepartmentID)
    VALUES 
    ("Alice", "Sanders", 101),
    ("Bob", "Johnson", 102),
    ("Charlie", "Smith", 103),
    ("Diana", "Brown", 101),
    ("Eve", "Davis", 102),
    ("Frank", "Miller", 103)''')

    cursor.execute('''SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
                      FROM Employees
                      JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID''')
    all_employees = cursor.fetchall()
    print("Список всех сотрудников:")
    for employee in all_employees:
        print(employee)

    cursor.execute('''SELECT Employees.FirstName, Employees.LastName 
                      FROM Employees
                      JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
                      WHERE Departments.DepartmentName = "IT"''')
    it_employees = cursor.fetchall()
    print("\nСотрудники, работающие в отделе IT:")
    for employee in it_employees:
        print(employee)
