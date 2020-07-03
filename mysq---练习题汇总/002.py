"""
题目描述
从titles表获取按照title进行分组，每组个数大于等于2，给出title以及对应的数目t。
CREATE TABLE IF NOT EXISTS "titles" (
`emp_no` int(11) NOT NULL,
`title` varchar(50) NOT NULL,
`from_date` date NOT NULL,
`to_date` date DEFAULT NULL);
如插入：
INSERT INTO titles VALUES(10001,'Senior Engineer','1986-06-26','9999-01-01');
INSERT INTO titles VALUES(10002,'Staff','1996-08-03','9999-01-01');
INSERT INTO titles VALUES(10003,'Senior Engineer','1995-12-03','9999-01-01');
INSERT INTO titles VALUES(10004,'Engineer','1986-12-01','1995-12-01');
INSERT INTO titles VALUES(10004,'Senior Engineer','1995-12-01','9999-01-01');
INSERT INTO titles VALUES(10005,'Senior Staff','1996-09-12','9999-01-01');
INSERT INTO titles VALUES(10005,'Staff','1989-09-12','1996-09-12');
INSERT INTO titles VALUES(10006,'Senior Engineer','1990-08-05','9999-01-01');
INSERT INTO titles VALUES(10007,'Senior Staff','1996-02-11','9999-01-01');
INSERT INTO titles VALUES(10007,'Staff','1989-02-10','1996-02-11');
INSERT INTO titles VALUES(10008,'Assistant Engineer','1998-03-11','2000-07-31');
INSERT INTO titles VALUES(10009,'Assistant Engineer','1985-02-18','1990-02-18');
INSERT INTO titles VALUES(10009,'Engineer','1990-02-18','1995-02-18');
INSERT INTO titles VALUES(10009,'Senior Engineer','1995-02-18','9999-01-01');
INSERT INTO titles VALUES(10010,'Engineer','1996-11-24','9999-01-01');
INSERT INTO titles VALUES(10010,'Engineer','1996-11-24','9999-01-01');

"""
#select title,count(title) from titles group by title having count(title)>=2;

