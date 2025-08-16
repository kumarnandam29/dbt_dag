create role if not exists dbt_role;
use role dbt_role;

-- I wanted to create the role inside the dbt_role but I doesn't have necessary priviliges, so i will go back to accountadmin and grant the access;
use role accountadmin;
grant create role on account to role dbt_role;

-- To drop the roles, db, wh
drop database if exists dbt_db;
drop role if exists dbt_role;
drop warehouse if exists dbt_wh;