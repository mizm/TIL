# SQL 기본

``` sql
-- Create
CREATE TABLE `sqlboard` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `title` varchar(255) UNIQUE,
  `query` varchar(5000),
  `varlist` varchar(1000),
  `created_at` DATETIME DEFAULT NOW(),
  `updated_at` DATETIME DEFAULT NOW(),
  `created_id` varchar(255),
  `updated_id` varchar(255)
);
-- update
UPDATE ZIMON_SQL_SQL SET VLIST=(#{varlist})WHERE CHILD_SQL = #{child}
-- alter
alter table user_group alter column userid varchar(40) not null;
-- Insert
Insert Into sqlboard values ()
insert into user_group values('219130', 1)
-- delete
DELETE FROM board where id = 10
-- join
select 
	u.id, 
	u.name, 
	g.name, 
	s.id, 
	s.title 
from USER_GROUP ug, sql_group sg, user u, "GROUP" g, sqlboard s 
where sg.GROUPDID  = ug.GROUPDID 
	and g.id = sg.GROUPDID  
	and s.id = sg.SQLID 
	and u.id = ug.userid;
	
select * from user_group as ug;
select * from sql_group as sg;
select * from user as u;
select * from "GROUP" as g;
-- select * from sqlboard as s;
select 
	u.id userid, 
	u.name username, 
	g.name groupname, 
	s.id queryid, 
	s.title querytitle 
from USER_GROUP ug, sql_group sg, user u, authgroup g, sqlboard s 
where sg.GROUPID  = ug.GROUPID 
	and g.id = sg.GROUPID  
	and s.id = sg.SQLID 
	and u.id = ug.userid 
	and u.id = '219180'
	group by queryid;


``alter
ALTER TABLE [테이블명] MODIFY ([컬럼명] DEFAULT [설정할 DEFAULT]);
```

