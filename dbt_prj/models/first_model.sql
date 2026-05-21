{{ config(materialized='table') }}

select 1 as id, 'hello dbt' as message