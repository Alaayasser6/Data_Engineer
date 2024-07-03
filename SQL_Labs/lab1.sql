---task list on product table
-- 1- list all products of adventureworks
-- 2- list red products
-- 3- list products with price greater than 5000
-- 4- list proucts that contains seat
-- 5- list products with price less than 1000 and contains lock
-- 6- list proucts start to be sold in 2008
-- 7- the sales at the start and the end of each month 
-------------------------------------------------------
use AdventureWorks2019
select *
from Production.Product
------------------------------------------------------------------------
-- 1- list all products of adventureworks
select Name
from Production.Product
------------------------------------------------------------------------
-- 2- list red products
select Color
from Production.Product
where Color = 'Red' 
 ------------------------------------------------------------------------
 -- 3- list products with price greater than 5000
 select ListPrice
 from Production.Product
 where ListPrice > 5000
 ------------------------------------------------------------------------
 -- 4- list proucts that contains seat
 select Name
 from Production.Product
 where Name like '%Seat%'
 ------------------------------------------------------------------------
 -- 5- list products with price less than 1000 and contains lock
 select Name ,ListPrice
 from Production.Product
 where Name like '%lock%' and ListPrice < 1000
 ------------------------------------------------------------------------
 -- 6- list proucts start to be sold in 2008
 select Name ,SellStartDate
from Production.Product 
where SellStartDate like '%2008%'
-------------------------------------------------------------------
-- 7- the sales at the start and the end of each month 
select TotalDue ,OrderDate , DAY(soh.OrderDate) as Day , MONTH(soh.OrderDate) Month, year(soh.OrderDate) Year
from Sales.SalesOrderHeader soh
where Day(OrderDate)=1 or Day(OrderDate)= Day(EOMONTH(OrderDate))