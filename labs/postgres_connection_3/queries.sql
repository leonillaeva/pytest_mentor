-- check the version
SELECT version();

/* SCHEMA TESTING */

SELECT * FROM information_schema.columns;

-- show all public tables info
select * from information_schema.tables
where table_schema='public';

-- show columns, data type in authentication_customuser
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'authentication_customuser';


-- number of columns in authentication_customuser
SELECT COUNT(column_name) AS number_columns
FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'authentication_customuser';

-- nullable columns
SELECT column_name, is_nullable
FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'authentication_customuser';

-- key_column_usage
SELECT constraint_name, column_name
FROM information_schema.key_column_usage
WHERE table_schema = 'public'
AND table_name = 'authentication_customuser';

-- constraint_type
SELECT constraint_name, constraint_type 
FROM information_schema.table_constraints 
WHERE table_name='authentication_customuser';

/* END of SCHEMA TESTING */

SELECT * FROM authentication_customuser;
SELECT * FROM book_book;
SELECT * FROM author_author;
SELECT * FROM author_author_books;
SELECT * FROM order_order;
SELECT * FROM auth_group;


SELECT id
	, first_name
	, last_name
	, role
FROM authentication_customuser
WHERE role  = 1;

SELECT * FROM information_schema.columns;

