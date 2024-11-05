/* 
prepared by: Alaa Yasser
This section contains tasks using windows functions (rank,sum,lag) 
*/

--1)monthly report for each product
select month(orderdate)month,p.ProductID,sum(orderqty) qty
from production.product p join sales.SalesOrderDetail sod
on p.ProductID=sod.ProductID
join Sales.SalesOrderHeader soh
on sod.SalesOrderID=soh.SalesOrderID
where year(OrderDate)=2012
group by month(orderdate),p.ProductID
order by month(orderdate),p.ProductID
------------------------------------------------------------------------------------------------------
--2)Running product sales for each month
with productsales (year,month,productid,sumlinetotal,runningsales)
as(
select YEAR(orderdate) ,month (orderdate) month,p.ProductID,sum (linetotal)sumlinetotal , sum(sum(linetotal)) over (partition by month(orderdate),year(orderdate) order by p.ProductID)
from production.product p join sales.SalesOrderDetail sod
on p.ProductID=sod.ProductID
join Sales.SalesOrderHeader soh
on sod.SalesOrderID=soh.SalesOrderID
group by YEAR(orderdate), month (orderdate),p.ProductID
)

select*
from productsales ;

/*select YEAR(orderdate) year ,month (orderdate) month,p.ProductID,sum (linetotal)sumlinetotal 
from production.product p join sales.SalesOrderDetail sod
on p.ProductID=sod.ProductID
join Sales.SalesOrderHeader soh
on sod.SalesOrderID=soh.SalesOrderID
group by p.ProductID,year(orderdate) ,month(orderdate)
order by ProductID,year ,month*/
------------------------------------------------------------------------------------------------------
--3)running product sales for each year

with productsales_year (year,productid,sumlinetotal,runningsales)
as(
select year (orderdate) year ,p.ProductID,sum (linetotal)sumlinetotal , sum(sum(linetotal)) over (partition by year(orderdate) order by p.ProductID)
from production.product p join sales.SalesOrderDetail sod
on p.ProductID=sod.ProductID
join Sales.SalesOrderHeader soh
on sod.SalesOrderID=soh.SalesOrderID
group by year(orderdate),p.ProductID
)
select*
from productsales_year;

------------------------------------------------------------------------------------------------------
--4)monthly growth rate for each product
with productsales (month,productid,sumlinetotal,lag)
as(
select month (orderdate) month,p.ProductID,sum (linetotal),
lag(sum (linetotal),1) over (order by p.productid,month (orderdate))

from production.product p join sales.SalesOrderDetail sod
on p.ProductID=sod.ProductID
join Sales.SalesOrderHeader soh
on sod.SalesOrderID=soh.SalesOrderID
where year (orderdate)=2012
group by month (orderdate),p.ProductID
)
select* ,sumlinetotal-lag 
from productsales p
order by p.productid ,p.month;
------------------------------------------------------------------------------------------------------
--5)Best salesperson for each product
with ranking (ProductID ,salespersonid,personsales,rank)
as(
select ProductID ,soh.salespersonid,sum(linetotal) personsales ,rank () over (partition by productid order by sum(linetotal) desc) rank
from Sales.SalesOrderHeader soh join sales.SalesOrderDetail sod
on soh.SalesOrderID=sod.SalesOrderID
where SalesPersonID is not null 
group by  ProductID ,soh.salespersonid
)
select * 
from ranking
where rank=1
order by  ProductID ,salespersonid

