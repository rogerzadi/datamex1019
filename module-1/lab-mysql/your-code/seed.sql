
mysql> INSERT INTO cars (ID,VIN,Manufacturer,Model,Year,ColorV) VALUES (0,"3K096I98581DHSNUP","Volkswagen","Tiguan",2019,"Blue");
Query OK, 1 row affected (0.08 sec)

mysql> ALTER TABLE Customers CHANGE Address Address VARCHAR(45);
Query OK, 0 rows affected (0.27 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> INSERT INTO Customers (ID,Customer_ID,Name,Phone,Email,Address,City,State,Country,Postal) VALUES (0,10001,"Pablo Picasso","+34 636 17 63 82","-","Paseo de la chopera,14", "Madrid","Madrid", "Spain", 28045);
Query OK, 1 row affected (0.09 sec)

mysql> INSERT INTO salespersons (ID,Staff_ID,Name,Store) VALUES (0,0001,"Petey Cruiser","Madrid");
Query OK, 1 row affected (0.09 sec)

mysql> INSERT INTO invoices (ID,Invoice_Number,Date,Car,Customer,Sales_Person) VALUES (0,852399038,"22-08-2018",0,1,3);
Query OK, 1 row affected (0.07 sec)
