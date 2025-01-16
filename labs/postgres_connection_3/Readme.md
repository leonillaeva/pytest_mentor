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

### DDL
- CREATE DATABASE db
- USE db
- DROP DATABASE db
- CREATE TABLE tbl_name(id INT, count INT)
- DROP TABLE tbl_name
- TRUNCATE TABLE tbl_name - удаление всех строк таблицы

### DML, CRUD акроним
- Create - INSERT
- Read - SELECT
- Update - UPDATE
- Delete - DELETE

## SQLAlchemy
***Простой Python. Современный стиль программирования***. *Второе издание. Билл Любанович. 2021.Гл.16, стр 349.*
DB-API дает ограниченный набор возможностей.

SQLAlchemy самая популярная библиотека для работы с разными бд.

Использовать SQLAlchemy можно на нескольких уровнях:
1. ***движок SQLAlchemy*** — самый низкий уровень управляет пулами соединений с бд, 
выполняет команды SQL и возвращает результат. Это ближе всего к DB-API.
- import sqlalchemy as sa
- conn = sa.create_engine('sqlite://)
- conn.execute("""CREATE ...""")
2. ***язык выражений SQL*** — позволяет выражать запросы более Python-ориентированным способом.
- import sqlalchemy as sa
- conn = sa.create_engine('sqlite://)
- meta = sa.MetaData()
- zoo = sa.Table('zoo', meta, sa.Column('critter', sa.String, primary_key=True)), sa.Column(...)

*---------- объект zoo промежуточное звено между SQL и Python*
- meta.create_all(conn)
- conn.execute(zoo.insert('bear', 2, 1000.0))
- result = conn.execute(zoo.select())
- rows = result.fetchall() - получить результат
3. ***SQLAlchemy ORM*** — самый высокий уровень. Это ORM (Object Relational Model — объектно-реляционная модель), 
использует язык выражений SQL Expression Language и связывает код приложения с реляционными структурами данных. 

Старается сделать реальные механизмы бд невидимыми.

Вы определяете классы, а ORM обрабатывает способ, с помощью которого они получают данные из бд и возвращают их обратно.
Основная идея, на которой базируется термин "объектно-реляционное отображение", заключается в том, что можно ссылаться
на объекты в коде и придерживаться таким образом принципов работы с Python, но при этом использовать реляционную бд.
*******************************************
import sqlalchemy as sa<br>
from sqlalchemy.orm import declarative_base<br>

conn = sa.create_engine('sqlite:///zoo.db') - использовать файл zoo.db<br>

Base = declarative_base()<br>

class Zoo(Base):<br>

&emsp;\r__tablename__ = 'zoo'<br>
&emsp;critter = sa.Column('critter', sa.String, primary_key=True))<br>
&emsp;count = sa.Column('count', sa.Integer)<br><br>

&emsp;def \r__init__(self, critter, count):<br>
&emsp;&emsp;self.critter = critter<br>
&emsp;&emsp;self.count = count<br>

&emsp;def \r__repr__(self):<br>
&emsp;&emsp; return "<Zoo({}, {},)>".format(self.critter, self.critter)<br>


Base.metadata.create_all(conn) - создает бд<br><br>

**** *coздаем сессию для коммуникации с бд* ****************************<br>
from sqlalchemy.orm import sessionmaker<br>
Session = sessionmaker(bind=conn)<br>
session = Session()<br><br>
**** *coздаем объекты, передаем в сессию* *********<br>
first = Zoo('first', 1)<br>
second = Zoo('second', 2)<br>
third = Zoo('third', 3)<br><br>

session.add(first)<br>
session.add_all(\[second, third])<br><br>
**** *завершаем сессию. Результат - создан файл zoo.db* *********<br>
session.commit()<br>

<hr> 

**** ***with***. *Usual case* *********<br>
from sqlalchemy import create_engine<br>

*--Create Engine object*<br>
engine = create_engine("postgresql+psycopg2://user:password@localhost/dbname")<br>

*--Working with db*<br>
with engine.connect() as connection:<br>
&emsp;    result = connection.execute("SELECT 1")<br>
&emsp;    print(result.scalar())<br>

*--Close pool connections*<br>
engine.dispose()<br>

## Commands
| Command         | Flag           | Description          |
|-----------------|----------------|----------------------|
| pytest          | -----          | Runs all tests       |
| pytest -m smoke | -m smoke       | Runs smoke tests     |
|pytest -m "not smoke"| -m "not smoke" | Excludes smoke tests |
|pytest tests\test_schema.py| -----          | CLI                  |
|pytest tests\test_schema.py::TestDbSchema| ----           | --Runs class         |
|pytest tests\test_schema.py::TestAuthenticationCustomuserSchema::test_get_count_column_names| ----           | Runs test in class   |





