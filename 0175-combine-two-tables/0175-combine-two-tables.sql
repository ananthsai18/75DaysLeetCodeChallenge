# Write your MySQL query statement below
Select a.firstName ,a.lastName , b.city,b.state
from person a
left join address b
on a.personId=b.personId;  