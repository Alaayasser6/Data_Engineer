/*
Topic: subquery
create by: Alaa Yasser
 Tasks:
	1- gender sales percentage of sales   
	2- marital status sales percentage of sales    
	3- compare between customer sales to total sales    
	4- compare between customer sales to total sales for each territory    
	5- sales growth rate through years                       
	6- products sold in 2014 but not in 2011 or 2012   */ 
---------------------------------------------------------------------------------------------------------
/*
1)gender sales percentage of sales
 gender         from       humanresource.employee
sum(totaldue)     from       sales.salesorderheader */
select gender , sum(totaldue) sum,
sum(totaldue)/(select sum(totaldue) from sales.salesorderheader)*100 percentage
from sales.salesorderheader soh join HumanResources.employee e
on soh.SalesPersonID = e.BusinessEntityID
group by e.Gender
-------------------------------------------------------------------------------------
--2)marital status sales percentage of sales
select MaritalStatus , sum(totaldue) sum,
sum(totaldue)/(select sum(totaldue) from sales.salesorderheader)*100 percentage
from sales.salesorderheader soh join HumanResources.employee e
on soh.SalesPersonID = e.BusinessEntityID
group by MaritalStatus
-------------------------------------------------------------------------------------
/* 3)compare between customer sales to total sales 
  customer      from      sales.salesorderheader
    totaldue      from      sales.salesorderheader */

select CustomerID , sum (TotalDue) customersales ,(select sum(totaldue) from sales.SalesOrderHeader) totalsales
from Sales.SalesOrderHeader
group by CustomerID
order by CustomerID 
-------------------------------------------------------------------------------------
-- 4) compare between customer sales to total sales for each territory
select st.name,CustomerID,sum (TotalDue) customersales,(select sum(totaldue) from sales.SalesOrderHeader) totalsales
from Sales.SalesOrderHeader  soh join sales.SalesTerritory st on st.TerritoryID=soh.TerritoryID  
group by CustomerID ,st.Name
order by st.name
-------------------------------------------------------------------------------------
-- 5) sales growth rate through years  
select year(orderdate), sum(totaldue) total ,
(select sum(totaldue) 
from sales.SalesOrderHeader 
where year(orderdate)=2011) total2011 ,
(sum(totaldue)-(select sum(totaldue) 
from sales.SalesOrderHeader 
where year(orderdate)=2011))/(select sum(totaldue) 
from sales.SalesOrderHeader 
where year(orderdate)=2011)*100 percentage
from sales.SalesOrderHeader
group by year(orderdate)
order by year(orderdate)
-------------------------------------------------------------------------------------
-- 6) products sold in 2014 but not in 2011 or 2012 
select distinct p.Name
from Production.Product p join sales.SalesOrderDetail sod
on p.productid=sod.ProductID
join Sales.SalesOrderHeader soh 
on soh.SalesOrderID=sod.SalesOrderID
where year(soh.OrderDate)=2011
except 
select distinct p.Name
from Production.Product p join sales.SalesOrderDetail sod
on p.productid=sod.ProductID
join Sales.SalesOrderHeader soh 
on soh.SalesOrderID=sod.SalesOrderID
where year(soh.OrderDate) in(2012,2014) 

