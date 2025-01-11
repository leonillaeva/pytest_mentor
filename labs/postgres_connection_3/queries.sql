-- check the version
SELECT version();

select * from information_schema.tables
where table_schema='public';


SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'authentication_customuser';

SELECT COUNT(column_name) AS number_columns
FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'authentication_customuser';

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