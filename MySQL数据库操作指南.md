MySQL数据库操作指南

```
(1)SQL语言主要分为：
    DQL：数据查询语言，用于对数据进行查询，如select
    DML：数据操作语言，对数据进行增加、修改、删除，如insert、update、delete
    TPL：事务处理语言，对事务进行处理，包括begin transaction、commit、rollback
    DCL：数据控制语言，进行授权与权限回收，如grant、revoke
    DDL：数据定义语言，进行数据库、表的管理等，如create、drop
    说明:
        对于程序员来讲，重点是数据的增、删、改、查，必须熟练编写DQL、DML，能够编写DDL完成数据库、表的操作，其它操作如TPL、DCL了解即可。
        SQL语言不区分大小写。
    
(2)MySQL数据库服务端软件的安装:
    sudo apt-get install mysql-server
    
    .显示安装包信息：
    ps -aux | grep mysql
    
    .查看MySQL服务状态:
    sudo service mysql status
    
    .停止MySQL服务:
    sudo service mysql stop
    
    .启动MySQL服务:
    sudo service mysql start
    
    .重启MySQL服务:
    sudo service mysql restart

    .配置文件路径为: /etc/mysql/mysql.conf.d/mysqld.cnf
        port:表示端口号，默认为3306
        bind-address:表示服务器绑定的ip，默认为127.0.0.1
        datadir:表示数据库保存路径，默认为/var/lib/mysql
        log_error:表示错误日志，默认为/var/log/mysql/error.log

(3)MySQL数据库客户端软件的安装:
    .常用的MySQL数据库客户端软件有：
        1，图形化界面客户端Navicat
        2，命令行客户端mysql

    .图形化界面客户端Navicat的使用
        1，可以到Navicat官网下载
        2，将文件拷贝到Ubuntu虚拟机中，放到桌面上
        3，运行命令：
        chmod +x navicat15-mysql-cs.AppImage
        ./navicat15-mysql-cs.AppImage

    .命令行客户端mysql的安装：
        sudo apt-get install mysql-client
        .显示安装包信息：
        apt-cache show mysql-client
        
        .mysql命令的使用帮助:
        mysql --help

    .MySQL客户端的使用:
        .MySQL客户端连接MySQL服务端命令
        mysql -uroot -p
        
        说明:
        -u: 表示MySQL服务端的用户名
        -p: 表示MySQL服务端的密码
        quit 或者 exit 或者 ctr + d 表示退出

(4)常用数据类型如下:
    整数：int，bit（二进制位）
    小数：decimal
    字符串：varchar,char
    日期时间: date, time, datetime
    枚举类型(enum)

    数据类型说明:
        decimal:表示浮点数，如 decimal(5, 2) 表示共存5位数，小数占 2 位.
        char:表示固定长度的字符串，如char(3)，如果填充'ab'时会补一个空格为'ab '，3表示字符数
        varchar:表示可变长度的字符串，如varchar(3)，填充'ab'时就会存储'ab'，3表示字符数
        对于图片、音频、视频等文件，不存储在数据库中，而是上传到某个服务器上，然后在表中存储这个文件的保存路径.
        字符串 text 表示存储大文本，当字符大于 4000 时推荐使用, 比如技术博客.

    常见的约束如下:
    主键 primary key: 物理上存储的顺序. MySQL 建议所有表的主键字段都叫 id, 类型为 int unsigned.
    非空 not null: 此字段不允许填写空值.
    惟一 unique: 此字段的值不允许重复.
    默认 default: 当不填写字段对应的值会使用默认值，如果填写时以填写为准.
    外键 foreign key: 对关系字段进行约束, 当为关系字段填写值时, 会到关联的表中查询此值是否存在, 如果存在则填写成功, 如果不存在则填写失败并抛出异常.

(5)数据库操作的SQL语句:
    .登录数据库:
    mysql -uroot -p
    
    说明:
    -u 后面是登录的用户名
    -p 后面是登录密码, 如果不填写, 回车之后会提示输入密码
    
    .登出(退出)数据库:
    quit 或 exit 或 ctrl + d
    
    .查看所有数据库:
    show databases;
    
    .创建数据库:
    create database 数据库名 charset=utf8;
    
    .使用数据库:
    use 数据库名;
    
    .查看当前使用的数据库:
    select database();
    
    .删除数据库-慎重:
    drop database 数据库名;


(6)表结构操作的SQL语句:
    .查看当前数据库中所有表:
    show tables;
    
    .创建表:
    create table 表名(
    字段名称 数据类型  可选的约束条件,
    column1 datatype contrai,
    ...
    );
    
    .添加字段:
    alter table 表名 add 列名 类型 约束;
    
    .修改字段类型:
    alter table 表名 modify 列名 类型 约束;
    
    说明:
    modify: 只能修改字段类型或者约束，不能修改字段名
    
    .修改字段名和字段类型:
    alter table 表名 change 原名 新名 类型及约束;
    
    说明:
    change: 既能对字段重命名又能修改字段类型还能修改约束
    
    .删除字段:
    alter table 表名 drop 列名;
    
    .查看创表SQL语句:
    show create table 表名;
    
    .查看创库SQL语句:
    show create database 数据库名;
    
    .查看表结构：
    desc 表名；
    
    .删除表:
    drop table 表名;

(7)表数据操作的SQL语句:
    1,查询数据:
        .查询所有列
        select * from 表名;
        
        .查询指定列
        select 列1,列2,... from 表名;
        
    2,添加数据
        .全列插入：值的顺序与表结构字段的顺序完全一一对应
        insert into 表名 values (...)
        
        .部分列插入：值的顺序与给出的列顺序对应
        insert into 表名 (列1,...) values(值1,...)
        
        .全列多行插入:
        insert into 表名 values(...),(...)...;
        
        .部分列多行插入:
        insert into 表名(列1,...) values(值1,...),(值1,...)...;
        
        说明:
        主键列是自动增长，但是在全列插入时需要占位，通常使用空值(0或者null或者default)
        在全列插入时，如果字段列有默认值可以使用 default 来占位，插入后的数据就是之前设置的默认值
        
    3,修改数据
    update 表名 set 列1=值1,列2=值2... where 条件
    
    4,删除数据
    delete from 表名 where 条件
    
    问题:
    上面的操作称之为物理删除，一旦删除就不容易恢复，我们可以使用逻辑删除的方式来解决这个问题。
    
    -- 添加删除表示字段，0表示未删除 1表示删除
    alter table students add isdelete bit default 0;
    
    -- 逻辑删除数据
    update students set isdelete = 1 where id = 8;
    
    说明:
    逻辑删除，本质就是修改操作

(8)as关键字
    1,使用 as 给字段起别名
    select id as 序号, name as 名字, gender as 性别 from students;
    
    2,通过 as 给表起别名
        -- 如果是单表查询 可以省略表名
        select id, name, gender from students;
        
        -- 表名.字段名
        select students.id,students.name,students.gender from students;
        
        -- 可以通过 as 给表起别名 
        select s.id,s.name,s.gender from students as s;

(9)distinct关键字
    distinct可以去除重复数据行
    select distinct 列1,... from 表名;
    当DISTINCT应用到多个字段时，其应用范围是其后面的所有字段，而不是紧挨它的一个字段
******************************************************************
<1>where语句支持的运算符:

    .比较运算符
    .逻辑运算符
    .模糊查询
    .范围查询
    .空判断

<2>where条件查询语法格式如下:
    select * from 表名 where 条件;
    
    1,比较运算符查询
        .等于: =
        .大于: >
        .大于等于: >=
        .小于: <
        .小于等于: <=
        .不等于: != 或 <>
        
    2,逻辑运算符查询
        .and
        .or
        .not
        
        说明:
        多个条件判断想要作为一个整体，可以结合‘()’。
        
    3,模糊查询
        .like:是模糊查询关键字
        
        .%:表示任意多个任意字符
        
        ._:表示一个任意字符
        
    4,范围查询
        .between .. and .. 表示在一个连续的范围内查询
        
        .in 表示在一个非连续的范围内查询
        
    5,空判断查询
        .判断为空使用: is null
        
        .判断非空使用: is not null
******************************************************************
[1]排序查询语法
    select * from 表名 order by 列1 asc|desc [,列2 asc|desc,...]
    
    语法说明:
        先按照列1进行排序，如果列1的值相同时，则按照列2排序，以此类推
        asc:从小到大排列，即升序
        desc:从大到小排序，即降序
        默认按照列值从小到大排序（即asc关键字）

[2]分页查询的语法
    select * from 表名 limit start,count
    
    说明:
        limit:是分页查询关键字
        start:表示开始行索引，默认是0
        count:表示查询条数

    已知每页显示m条数据，求第n页显示的数据
    提示: 关键是求每页的开始行索引
    
    查询学生表，获取第n页数据的SQL语句:
    
    select * from students limit (n-1)*m,m

[3]常用的聚合函数:
    .count(col): 表示求指定列的总行数
    .max(col): 表示求指定列的最大值
    .min(col): 表示求指定列的最小值
    .sum(col): 表示求指定列的和
    .avg(col): 表示求指定列的平均值
    
    聚合函数的特点
    聚合函数默认忽略字段为null的记录 要想列值为null的记录也参与计算，必须使用ifnull函数对null值做替换
    
    1,求总行数
    
    -- 返回非NULL数据的总行数
    select count(列名1) from 表名;
    
    -- 返回总行数，包含null值记录;
    select count(*) from 表名;

    2,求最大值
    select max(列名1) from 表名 where 条件;
    
    3,求最小值
    select min(列名1) from 表名 where 条件;
    
    4,求和
    select sum(列名1) from 表名 where 条件;
    
    5,求平均值,聚合函数不统计null值
    ifnull函数: 表示判断指定字段的值是否为null，如果为空使用自己提供的值
    
    select avg(ifnull (列名,0)) from 表名 where 条件 ;
    
	6，保留两位小数
	round(avg(列名),2)
	
[4]分组查询基本的语法格式如下：
    GROUP BY 列名 [HAVING 条件表达式] [WITH ROLLUP]
    
    说明:
        列名: 是指按照指定字段的值进行分组。
        HAVING 条件表达式: 用来过滤分组后的数据。
    	WITH ROLLUP：在所有记录的最后加上一条记录，显示select查询时聚合函数的统计和计算结果
    	
    1，group by的使用
    group by可用于单个字段分组，也可用于多个字段分组
    select 列名1，列名2 from 表名 group by 列名1，列名2;
    
    2，group by + group_concat()的使用
    group_concat(字段名): 统计每个分组指定字段的信息集合，每个信息之间使用逗号进行分割
    
    select 列名1,group_concat(列名2) from 表名 group by 列名1;
    
    3，group by + 聚合函数的使用
    select 列名1,avg(列名2) from 表名 group by 列名1;
    
    4，group by + having的使用
    having作用和where类似都是过滤数据的，但having是过滤分组数据的，只能用于group by
    
    select 列名1，列名2  from 表名 group by 列名1 having 条件;
    
    5， group by + with rollup的使用
    with rollup的作用是：在最后记录后面新增一行，显示select查询时聚合函数的统计和计算结果
    
    select 列名1,group_concat(列名2) from 表名 group by 列名1 with rollup;

[5]连接查询可以分为:
    .内连接查询
    .左连接查询
    .右连接查询
    .自连接查询
    .多表连接查询

    1.内连接查询语法格式:
    select 字段 from 表1 inner join 表2 on 表1.字段1 = 表2.字段2
    
    说明:
        inner join: 就是内连接查询关键字
        on: 就是连接查询条件

    2.左连接查询语法格式:
    select 字段 from 表1 left join 表2 on 表1.字段1 = 表2.字段2
    
    说明:
        left join: 就是左连接查询关键字
        on: 就是连接查询条件
        表1: 是左表
        表2: 是右表

    3.右连接查询语法格式:
    select 字段 from 表1 right join 表2 on 表1.字段1 = 表2.字段2
    
    说明:
        right join: 就是右连接查询关键字
        on: 就是连接查询条件
        表1: 是左表
        表2: 是右表

    4.自连接查询
    左表和右表是同一个表，根据连接查询条件查询两个表中的数据。
    
    自连接查询的用法:
    select c.列名1, c.列名2, c.列名3, p.列名1 from 表1 as 别名1 inner join 表1 as 别名2 on 别名1.列名3 = 别名2.列名1 where 条件;
    
    说明:
    自连接查询必须对表起别名
    5.多表连接查询：
    将其中的两个表连接后作为一个表，和第三表连接；
    查找所有员工的last_name和first_name以及对应的dept_name，也包括暂时没有分配部门的员工
        CREATE TABLE `departments` (
        `dept_no` char(4) NOT NULL,
        `dept_name` varchar(40) NOT NULL,
        PRIMARY KEY (`dept_no`));
        CREATE TABLE `dept_emp` (
        `emp_no` int(11) NOT NULL,
        `dept_no` char(4) NOT NULL,
        `from_date` date NOT NULL,
        `to_date` date NOT NULL,
        PRIMARY KEY (`emp_no`,`dept_no`));
        CREATE TABLE `employees` (
        `emp_no` int(11) NOT NULL,
        `birth_date` date NOT NULL,
        `first_name` varchar(14) NOT NULL,
        `last_name` varchar(16) NOT NULL,
        `gender` char(1) NOT NULL,
        `hire_date` date NOT NULL,
        PRIMARY KEY (`emp_no`));
    select last_name,first_name,dept_name from employees as e left join (select emp_no,dept_name from dept_emp as d1 left join departments as d2  on d1.dept_no =d2.dept_no) as f on e.emp_no = f.emp_no ;
[6]主查询和子查询的关系:
    .子查询是嵌入到主查询中
    .子查询是辅助主查询的,要么充当条件,要么充当数据源
    .子查询是可以独立存在的语句,是一条完整的 select 语句
******************************************************************
(1)数据库设计之三范式
    .第一范式（1NF）: 强调的是列的原子性，即列不能够再分成其他几列。
    .第二范式（2NF）: 满足 1NF，另外包含两部分内容，一是表必须有一个主键；二是非主键字段 必须完全依赖于主键，而不能只依赖于主键的一部分。
    .第三范式（3NF）: 满足 2NF，另外非主键列必须直接依赖于主键，不能存在传递依赖。即不能存在：非主键列 A 依赖于非主键列 B，非主键列 B 依赖于主键的情况。

(2)E-R模型即实体-关系模型，E-R模型就是描述数据库存储数据的结构模型。
    .E-R模型的使用场景:
        1.对于大型公司开发项目，我们需要根据产品经理的设计，我们先使用建模工具, 如:power designer，db desinger等这些软件来画出实体-关系模型(E-R模型)
    	2.然后根据三范式设计数据库表结构
        说明:
            实体: 用矩形表示，并标注实体名称
            属性: 用椭圆表示，并标注属性名称，
            关系: 用菱形表示，并标注关系名称
    1，一对一
    
    说明:
        .关系也是一种数据，需要通过一个字段存储在表中
        .1对1关系，在表A或表B中创建一个字段，存储另一个表的主键值
        
    2，一对多
    
    说明:
    	1对多关系，在多的一方表(学生表)中创建一个字段，存储班级表的主键值
    	
    3，多对多
    
    说明:
    	多对多关系，新建一张表C，这个表只有两个字段，一个用于存储A的主键值，一个用于存储B的主键值

(3)外键SQL语句的编写
    1.对于已经存在的字段添加外键约束：
    alter table 从表 add foreign key(外键字段) references 主表(主键字段);
    
    2.在创建数据表时设置外键约束：
    create table 表名1(
        ……
        字段1 类型 约束 , 
        字段2 类型 约束 ,
        字段3 类型 约束 , 
        foreign key(字段3) references 表名2(字段)
        ……
    );

    3.删除外键约束：
    -- 需要先获取外键约束名称,该名称系统会自动生成,可以通过查看表创建语句来获取名称
    show create table 表名;
    
    -- 获取名称之后就可以根据名称来删除外键约束
    alter table 表名 drop foreign key 外键名;
******************************************************************
{1}将查询结果插入到其它表中

	insert into 表名（字段） select 查询语句； 
	表示: 把查询结果插入到指定表中，也就是表复制。
	
	说明：select 查询语句；该语句可以理解为,新表中某列，和查询语句的某列，实现一个复制的过程；
	
	.insert into goods_cate(name) select cate_name from goods group by cate_name;
	
{2}使用连接更新表中某个字段数据

	update 表名1 as 表名11 inner join 表名2 as 表名22 on 表名11.字段 = 表名22.字段 set 表名11.字段 = 表名22.字段；
	
	说明：表名1 as 表名11 inner join 表名2 as 表名22 on 表名11.字段 = 表名22.字段；该语句可以当成一个表；
	
	.update goods as g inner join good_brands gb on g.brand_name = gb.name set g.brand_name = gb.id;
	
{3}创建表并给某个字段添加数据

	create table 表名（字段1 类型 约束 ，字段2 类型 约束，，，） select 查询语句 
	表示创建表并插入数据
	
	说明：select 查询语句；该语句可以理解为新表中某列，和查询语句的某列，实现一个复制的过程；
    
	.create table good_brands (     
id int unsigned primary key auto_increment,     
name varchar(40) not null) select brand_name as name from goods group by brand_name;

{4}修改表结构

	alter table 表名 change 原名1 新名1 类型 约束，change 原名2 新名2 类型 约束 ,,,
	
    说明：alter table 语句，可以同时修改多个字段信息,多个修改字段之间使用逗号分隔
    
    .alter table goods change cate_name cate_id int not null,change brand_name brand_id int not null;
    
{5}事务
    1.查看MySQL数据库支持的表的存储引擎:
    show engines;
    说明：
    	InnoDB:DEFAULT,Supports transactions, row-level locking, and foreign keys 
        常用的表的存储引擎是 InnoDB 和 MyISAM
        InnoDB 是支持事务的
        MyISAM 不支持事务，优势是访问速度快，对事务没有要求或者以select、insert为主的都可以使用该存储引擎来创建表
        
    2.通过创表语句可以得知，表的存储引擎是默认InnoDB。
    show create table 表名;
    
    3.修改表的存储引擎: 
    alter table 表名 engine = 引擎类型;
	
	4.开启事务:
        begin;
        或者
        start transaction;
    	说明:
            .开启事务后执行修改命令，变更数据会保存到MySQL服务端的缓存文件中，而不维护到物理表中；
            .MySQL数据库默认采用自动提交(autocommit)模式，如果没有显示的开启一个事务,那么每条sql语句都会被当作一个事务执行提交的操作;
            .当设置autocommit=0就是取消了自动提交事务模式，直到显示的执行commit和rollback表示该事务结束。
                set autocommit = 0 表示取消自动提交事务模式，需要手动执行commit完成事务的提交;
	5.提交事务：
		commit;
	6.回滚事务:
		rollback
{6}索引
	.查看表中已有索引:
	show index from 表名;
		说明:
			主键列会自动创建索引
	.索引的创建:
		alter table 表名 add index 索引名[随意](列名, ..)；
         说明:
             索引名不指定，默认使用字段名
	.索引的删除:
		alter table 表名 drop index 索引名;
	.联合索引
		alter table teacher add index (列名, ..);
        说明：
            联合索引又叫复合索引，即一个索引覆盖表中两个或者多个字段，一般用在多个字段一起查询的时候。
        联合索引的好处:
            减少磁盘空间开销，因为每创建一个索引，其实就是创建了一个索引文件，那么会增加磁盘空间的开销。
	.联合索引的最左原则
		在使用联合索引的时候，我们要遵守一个最左原则,即index(name,age)支持 name 、name 和 age 组合查询,而不支持单独 age 查询，因为没有用到创建的联合索引。
		说明:
		在使用联合索引的查询数据时候一定要保证联合索引的最左侧字段出现在查询条件里面，否则联合索引失效
{7}PyMySQL的使用
	1.安装pymysql第三方包:
	sudo pip3 install pymysql;
	
	说明:
        .安装命令: sudo pip3 install 第三方包名
        .卸载命令: sudo pip3 uninstall 第三方包名
        .命令查看第三方包的信息:pip3 show pymysql 
        .查看使用pip命令安装的第三方包列表:pip3 list
        
	2.pymysql的使用:
		1.导入 pymysql 包:
		import pymysql;
		
		2.创建连接对象:
		调用pymysql模块中的connect()函数来创建连接对象,代码如下:
							 conn=connect(host='localhost',port=3306,user='root',password='mysql',database='jingdong',charset='utf8')

             * 参数host：连接的mysql主机，如果本机是'localhost'
             * 参数port：连接的mysql主机的端口，默认是3306
             * 参数user：连接的用户名
             * 参数password：连接的密码
             * 参数database：数据库的名称
             * 参数charset：通信采用的编码方式，推荐使用utf8
             
             连接对象操作说明:
                  关闭连接 conn.close()
                  提交数据 conn.commit()
                  撤销数据 conn.rollback()
                  
          3.获取游标对象
                cursor =conn.cursor()
                
                游标操作说明:
                    .使用游标执行SQL语句:
                        .execute(operation [parameters ]) 执行SQL语句，
                        .返回受影响的行数，
                        .主要用于执行insert、update、delete、select等语句
                        
                        cursor.execute('sql语句')
                        
                        说明：以下可以防止sql注入
                        id = input('请输入您要查询的id:')
                        sql= 'select ,,, where id = %s'
                    	cursor.execute(sql,(id,))
                    	
                    .获取查询结果集中的一条数据:
                    
                    	cursor.fetchone()
                    	
                    	.返回一个元组, 如 (1,'张三'),间接判断是否有数据；
                    .获取查询结果集中的所有数据:
                    
                        cursor.fetchall()
                        
                        返回一个元组,如((1,'张三'),(2,'李四'))
                    .关闭游标:
                        cursor.close()
                        表示和数据库操作完成
	3.防止SQL注入
        .什么是SQL注入?
        	用户提交带有恶意的数据与SQL语句进行字符串方式的拼接，从而影响了SQL语句的语义，最终产生数据泄露的现象。
        .如何防止SQL注入?
            SQL语句参数化
            SQL语言中的参数使用%s来占位，此处不是python中的字符串格式化操作
            将SQL语句中%s占位所需要的参数存在一个列表中，把参数列表传递给execute方法中第二个参数
            说明:
            execute方法中的 %s 占位不需要带引号
    	
```

