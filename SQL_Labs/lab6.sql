/*
prepared by: Alaa Yasser

Tasks 
	1- rank products in each territory 
	2- list top 3 products at each territory
	3- list top 3 products at each territory for year 2013 and product sales > 100000
	4- list products in each categor
	5- sales of each product and its category 
	6- sales of each product and its category  for year 2012 and sales > 1000000
	7- sales of each product and its category  for year 2012 and sales > 1000000 and display running total for each category */
---------------------------------------------------------------------------------------------------------------------------------------
-- 1- rank products in each territory 
select ProductID ,territoryid,sum(linetotal) sum, rank() over (partition by territoryid order by  sum(linetotal))  ranking
from sales.SalesOrderHeader soh join Sales.SalesOrderDetail sod 
on soh.SalesOrderID=sod.SalesOrderID
group by territoryid,ProductID;

-- 2- list top 3 products at each territory
with ranking (ProductID,territoryid,sum,ranking)
as (select ProductID ,territoryid,sum(linetotal) sum, rank() over (partition by territoryid order by  sum(linetotal))  ranking
from sales.SalesOrderHeader soh join Sales.SalesOrderDetail sod 
on soh.SalesOrderID=sod.SalesOrderID
group by territoryid,ProductID)

select *
from ranking
where ranking.ranking in(1,2,3)

-- 3- list top 3 products at each territory for year 2013 and product sales > 100000
 with ranking (ProductID,territoryid,sum,ranking)
as (select ProductID ,territoryid,sum(linetotal) sum, rank() over (partition by territoryid order by  sum(linetotal))  ranking
from sales.SalesOrderHeader soh join Sales.SalesOrderDetail sod 
on soh.SalesOrderID=sod.SalesOrderID
where year(orderdate)=2013 
group by territoryid,ProductID
having sum(linetotal) > 100000 )
select *
from ranking
where ranking.ranking in(1,2,3)

-- 4- list products in each category
select p.ProductID,ps.Name ,ps.ProductSubcategoryID
from  Production.Product p  join Production.ProductSubcategory ps 
on ps.ProductSubcategoryID=p.ProductSubcategoryID
where p.ProductSubcategoryID is not null
order by  ps.ProductSubcategoryID ,ProductID
------------------------------------------------------------
select ProductID,ProductSubcategoryID,
rank()over(partition by ProductSubcategoryID  order by ProductID ) ranking 
from Production.Product
where ProductSubcategoryID is not null
order by ProductSubcategoryID
------------------------------------------------------------

-- 5-sales of each product and its category 
select p.ProductID,ps.Name ,ps.ProductSubcategoryID ,sum (linetotal)sum_of_each_product
from  Production.Product p  join Production.ProductSubcategory ps 
on ps.ProductSubcategoryID=p.ProductSubcategoryID
join sales.SalesOrderDetail sod 
on sod.ProductID=p.ProductID
where p.ProductSubcategoryID is not null
group by p.ProductID,ps.Name ,ps.ProductSubcategoryID 
order by  ps.ProductSubcategoryID ,ProductID
------------------------------------------------------------

-- 6- sales of each product and its category  for year 2012 and sales > 1000000
select p.ProductID,ps.Name ,ps.ProductSubcategoryID ,sum (linetotal)sum_of_each_product
from  Production.Product p  join Production.ProductSubcategory ps 
on ps.ProductSubcategoryID=p.ProductSubcategoryID
join sales.SalesOrderDetail sod 
on sod.ProductID=p.ProductID
join sales.SalesOrderHeader soh
on soh.SalesOrderID=sod.SalesOrderID
where p.ProductSubcategoryID is not null 
and year(soh.OrderDate)=2012 
group by p.ProductID,ps.Name ,ps.ProductSubcategoryID 
having  sum (linetotal) > 1000000
order by  ps.ProductSubcategoryID ,ProductID
------------------------------------------------------------

-- 7- sales of each product and its category  for year 2012 and sales > 1000000 and display running total for each category
select p.ProductID,ps.Name ,ps.ProductSubcategoryID ,sum (linetotal)sum_of_each_product,sum (sum (linetotal)) over (order by p.ProductID)
from  Production.Product p  join Production.ProductSubcategory ps 
on ps.ProductSubcategoryID=p.ProductSubcategoryID
join sales.SalesOrderDetail sod 
on sod.ProductID=p.ProductID
join sales.SalesOrderHeader soh
on soh.SalesOrderID=sod.SalesOrderID
where p.ProductSubcategoryID is not null 
and year(soh.OrderDate)=2012 
group by p.ProductID,ps.Name ,ps.ProductSubcategoryID 
having  sum (linetotal) > 1000000
order by  ps.ProductSubcategoryID ,ProductID