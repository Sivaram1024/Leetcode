# Write your MySQL query statement below
SELECT person.firstname, person.lastname, Address.city, Address.state
FROM Person
Left join Address
on Person.personid = Address.personid;