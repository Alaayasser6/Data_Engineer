--1)customer report (sales,percentage of sales for territoryid=1 and year=2012)
--2)compair salesperson performance quarter for 2013
--3)product performance salse quarter for 2013



--1)customer report (sales,number of product,percentage of product,percentage of sales for territoryid=1 and year=2012)) 
/* customerid   from    sales.salesorderheader
   territortid  from    sales.salesorderheader
   productid    from    sales.salesorderdetail
   join on salesorderid */

------------------------------------------------
--customer sales
   select count (productid)totalproduct
   from sales.salesorderheader soh join sales.SalesOrderDetail sod
   on  soh.SalesOrderID=sod.SalesOrderID
   where TerritoryID=1  and year (orderdate)=2012
   group by TerritoryID;
--------------------------------------------------------------------------------------------------
  with t_sales (t_sales)
  as(select sum (LineTotal)
   from sales.salesorderheader soh join sales.SalesOrderDetail sod
   on  soh.SalesOrderID=sod.SalesOrderID
   where TerritoryID=1  and year (orderdate)=2012
   group by TerritoryID),

 c_sales  (c_ID , c_sales) as  (select CustomerID ,sum(LineTotal)
   from sales.salesorderheader soh join sales.SalesOrderDetail sod
   on  soh.SalesOrderID=sod.SalesOrderID
   where TerritoryID=1 and year(OrderDate)=2012
   group by CustomerID)
   
   select c_sales.c_Id ,(c_sales.c_sales/t_sales.t_sales *100) persentage
   from c_sales,t_sales
   order by c_ID

----------------------------------------------------------------------------------------------------------
 --2)compair salesperson performance quarter for 2013
 with quarter1 (salesprsonID,quarter1)
 as (select SalesPersonID,sum (totaldue)
 from sales.salesorderheader soh
 where DATEPART(quarter,OrderDate)=1 and year(orderdate)=2013
 group by SalesPersonID),

quarter2(salespersonID , quarter2)
as (select SalesPersonID,sum (totaldue)
 from sales.salesorderheader soh
 where DATEPART(quarter,OrderDate)=2 and year(orderdate)=2013
 group by SalesPersonID) ,

 quarter3 (salespersonID , quarter3)
as (select SalesPersonID,sum (totaldue)
 from sales.salesorderheader soh
 where DATEPART(quarter,OrderDate)=3 and year(orderdate)=2013
 group by SalesPersonID),
 quarter4(salespersonID , quarter4)
as (select SalesPersonID,sum (totaldue)
 from sales.salesorderheader soh
 where DATEPART(quarter,OrderDate)=3 and year(orderdate)=2013
 group by SalesPersonID)

 select *
 from quarter1 q1 join quarter2 q2 on q1.salesprsonID=q2.salespersonID
 join quarter3 q3 on q2.salespersonID=q3.salespersonID 
 join quarter4 q4 on q3.salespersonID=q4.salespersonID
 order by q4.salespersonID
 ----------------------------------------------------------------------------------------------------------------
 --3)product performance salse quarter for 2013
  with quarter1 (productID,quarter1)
 as (select productid,count (ProductID)
 from sales.salesorderheader soh join sales.SalesOrderDetail sod 
 on sod.SalesOrderID=soh.SalesOrderID
 where DATEPART(quarter,OrderDate)=1 and year(orderdate)=2013
 group by ProductID),

  quarter2 (productID,quarter2)
 as (select productid,count (ProductID)
 from sales.salesorderheader soh join sales.SalesOrderDetail sod 
 on sod.SalesOrderID=soh.SalesOrderID
 where DATEPART(quarter,OrderDate)=2 and year(orderdate)=2013
 group by ProductID),
 
  quarter3 (productID,quarter3)
 as (select productid,count (ProductID)
 from sales.salesorderheader soh join sales.SalesOrderDetail sod 
 on sod.SalesOrderID=soh.SalesOrderID
 where DATEPART(quarter,OrderDate)=3 and year(orderdate)=2013
 group by ProductID),

  quarter4 (productID,quarter4)
 as (select productid,count (ProductID)
 from sales.salesorderheader soh join sales.SalesOrderDetail sod 
 on sod.SalesOrderID=soh.SalesOrderID
 where DATEPART(quarter,OrderDate)=4 and year(orderdate)=2013
 group by ProductID)

  select q1.productID,q1.quarter1,q2.quarter2,q3.quarter3,q4.quarter4
 from quarter1 q1 join quarter2 q2 on q1.ProductID=q2.ProductID
 join quarter3 q3 on q2.ProductID=q3.ProductID
 join quarter4 q4 on q3.ProductID=q4.ProductID
 order by q4.ProductID
