# Database Testing
1. [Database Testing: What it is, Why & Best Practices](https://testsigma.com/blog/database-testing/)
2. [Database Testing: A Full Guide](https://katalon.com/resources-center/blog/database-testing)
3. [Tutorial Database Testing using SQL. QATestLab](https://qatestlab.com/resources/knowledge-center/tutorial-database-testing-using-sql/)

## Types of Database Testing
- Structural Testing
- Functional Testing
- Non-functional Testing

### 1. Structural Testing
Structural testing, also known as glass box testing or white-box testing, focuses on examining the internal structure of the system (which is the database and its components in this case). The goal is to ensure that the database schema, tables, relationships, constraints, and other structural elements are designed and implemented correctly.

Several types of structural testing include:
- Table and Column Validation
- Stored Procedures and Function Testing
- Index Testing
- Data Migration Testing
- Schema Testing
- Database Server Validation
### 2. Functional Testing
For database testing specifically, functional testing focuses more on the functional aspects of the database, ensuring that it can perform its intended purposes
- SQL Query Testing
- Transaction Testing
- Data Validation
- Data Manipulation Testing
- Data Retrieval Testing
### 3. Non-functional Testing
In the scope of this type, we focus on performance testing, load testing, stress testing, security testing, and any type of testing whose scope goes beyond the core functionalities, ensuring that these non-functional aspects of the database meet the business requirements.
- Performance testing
- Load Testing
- Stress Testing
- Security Testing
## What is ETL testing? Is ETL testing similar to database testing?
ETL (Extract, Transform, Load) testing is a subset of database testing that focuses on verifying the data extraction, transformation, and loading processes within a data integration pipeline. ETL testing is much more specific, focusing on the data movement and transformation process, while database testing encompasses the entire range of testing activities in the database.

## [PostgreSQL – Naming Conventions](https://www.geeksforgeeks.org/postgresql-naming-conventions/)
### Basic Naming Conventions in PostgreSQL
When creating database object names in PostgreSQL, consider the following basic conventions:

1. Table Names
- Use **plural nouns** for table names to indicate that they contain multiple records.
- Use **snake_case** to separate words.
2. Column Names
- Use **descriptive** names that indicate the data being stored.
- Use **snake_case** for consistency.

## DB_API
***Простой Python. Современный стиль программирования***. *Второе издание. Билл Любанович. 2021.Гл.16, стр 345.*
 
[PEP 249 -- Python Database API Specification v2.0](https://legacy.python.org/dev/peps/pep-0249/)

DB-API — это стандартный API в Python, предназначенный для получения доступа к реляционным базам данных. 
Основные функции:
* [connect()](https://legacy.python.org/dev/peps/pep-0249/#connection-objects) — создание соединения с бд. 
Может включать аргументы: имя пользователя, пароль, адрес сервера и пр.;<br>
**Connection Objects**. Connection methods: 
1. .close(), 
2. .commit(), 
3. .rollback(), 
4. .cursor()

* [cursor()](https://legacy.python.org/dev/peps/pep-0249/#cursor-objects) — создание объекта курсора, предназначенного для работы с запросами;<br>
These objects represent a database cursor, which is used to manage the context of a fetch operation.<br>
**Cursor Objects**. Cursor methods: 
1. .close(), 
2. .execute(operation \[, parameters]), 
3. .executemany( operation, seq_of_parameters ),
4. .fetchone(),
5. .fetchmany(\[size=cursor.arraysize]),
6. .fetchall(),
7. .nextset(),
8. .arraysize
9. .callproc( procname \[, parameters ] ) - optional, 

* execute(), executemany() — запуск одной или нескольких команд SQL. *Метод курсора.*
[Prepare and execute a database operation (query or command)](https://legacy.python.org/dev/peps/pep-0249/#id15)
* fetchone(), fetchmany(), fetchall() — получение результатов функции execute(). *Метод курсора.*

## DDL
- CREATE DATABASE db
- USE db
- DROP DATABASE db
- CREATE TABLE tbl_name(id INT, count INT)
- DROP TABLE tbl_name
- TRUNCATE TABLE tbl_name - удаление всех строк таблицы

## DML, CRUD акроним
- Create - INSERT
- Read - SELECT
- Update - UPDATE
- Delete - DELETE

