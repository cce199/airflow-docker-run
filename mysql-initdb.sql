select @@version;
select current_timestamp();

grant all privileges on airflow.* to root1@'%' with grant option;
create database airflow;
show global variables like '%timestamp%';
