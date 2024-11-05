-- 1- customers who made sales greater than 100000 in territoryid 5,6
-- 2- list sales in 2013 by quarters
-- 3- list our sales in weekend days for june 2012
-- 4- Age of our employees

use AdventureWorks2019
-- 1- customers who made sales greater than 100000 in territoryid 5,6
select CustomerID ,sum(TotalDue) totaldue
from Sales.SalesOrderHeader
where TerritoryID in (5,6) 
group by CustomerID
having sum(TOtalDue)>100000

-- 2- list sales in 2013 by quarters
select datepart(quarter,orderdate) qtr ,sum(TotalDue)
from Sales.SalesOrderHeader
where YEAR(orderdate)=2013
group by datepart(quarter,orderdate)
order by datepart(quarter,orderdate)

-- 3- list our sales in weekend days for june 2012
select SalesOrderID ,datename(weekday,orderdate) day ,datename(month,orderdate) month,  datename(year,orderdate) year
from sales.salesorderheader
where day(orderdate) in (1,2) and MONTH(orderdate) =6 and year(orderdate)=2012
order by SalesOrderID,datename(WEEKDAY,orderdate)

-- 4- Age of our employees
select CONCAT(firstname,'_',lastname) name, BirthDate ,DATEDIFF(year,BirthDate,GETDATE()) Age
from person.Person ,humanresources.Employee
order by DATEDIFF(year,BirthDate,GETDATE()) 