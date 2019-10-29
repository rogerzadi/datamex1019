 
mysql> CREATE TABLE cars (ID VARCHAR(20), VIN VARCHAR(20), Manufacturer VARCHAR(20), Model VARCHAR(20), Year VARCHAR(20), ColorV VARCHAR(20));
Query OK, 0 rows affected (1.38 sec)


mysql> CREATE TABLE customers (ID VARCHAR(20), Customer_ID VARCHAR(20), Name VARCHAR(20), Phone VARCHAR(20), Email VARCHAR(20), Address VARCHAR(20), City VARCHAR(20), State VARCHAR(20), Country VARCHAR(20), Postal VARCHAR(20));
Query OK, 0 rows affected (0.43 sec)

mysql> CREATE TABLE Salespersons (ID VARCHAR(20), Staff_ID VARCHAR(20), Name VARCHAR(20), Store VARCHAR(20));
Query OK, 0 rows affected (0.57 sec)

mysql> CREATE TABLE Invoices (ID VARCHAR(20), Invoice_Number VARCHAR(20), Date VARCHAR(20), Car VARCHAR(20), Customer VARCHAR(20), Sales_Person VARCHAR(20));
Query OK, 0 rows affected (0.65 sec)