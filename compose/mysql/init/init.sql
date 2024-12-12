# compose/mysql/init/init.sql
Alter user 'dbuser'@'%' IDENTIFIED WITH mysql_native_password BY 'As87s_@65jdsa';
GRANT ALL PRIVILEGES ON 3dannotate.* TO 'dbuser'@'%';
GRANT FILE ON *.* TO 'dbuser'@'%';
FLUSH PRIVILEGES;