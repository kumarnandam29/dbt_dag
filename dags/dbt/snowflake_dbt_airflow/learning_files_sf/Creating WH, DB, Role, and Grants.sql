use role accountadmin;

create warehouse dbt_wh with warehouse_size='x-small';

create database dbt_db;
create role dbt_role;

show grants on warehouse dbt_wh;

-- Now dbt_wh has only access to accountadmin, we can give access to dbt_role
grant usage on warehouse dbt_wh to role dbt_role;
show grants on warehouse dbt_wh;

-- Now giving the grants to one more user
grant usage on warehouse dbt_wh to user kumarnandam29;
show grants on warehouse dbt_wh;

-- Giving grants to all on database 
grant all on database dbt_db to role dbt_role;

-- using the role dbt_role: we need to assign the role to the current user before using this.
grant role dbt_role to user kumarnandam29;
use role dbt_role;

