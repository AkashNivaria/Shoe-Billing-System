use shoebilling;
create table store
(Pcode int(9),
Pname varchar(100),
Price int(7),
Category varchar(10),
Gender varchar(10));


LOAD DATA INFILE "C:\Users\hp\Desktop\Project for Intership\Shoe.csv"
INTO TABLE store
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
