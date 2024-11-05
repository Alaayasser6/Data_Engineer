-- 1- compare sales according to :
--	-Gender
--  -Marital Status
-- 2- top3 products at eah territory for 2013                          out of scope
-- 3- how many employees for each jobtitle                           
-- 4- list top product name for each year ,how many and how much      out of scope 
-- 5- list sales persons who sold product called "AWC Logo Cap" how many and how much

select *
from sales.SalesPerson

-- 1- compare sales according to :
/*Gender               from     humanresource.employee
  Marital Status       from     humanresource.employee
salesorderid           from     sales.salesorderheader  */

select HRE.Gender,HRE.MaritalStatus, COUNT(SOH.salesorderid) numberofsales
FROM HumanResources.Employee HRE
	JOIN Sales.SalesOrderHeader SOH
		ON HRE.BusinessEntityID = soh.SalesPersonID
group by  HRE.Gender,HRE.MaritalStatus
order by HRE.MaritalStatus
--------------------------------------------------------------------------------------------------------------
-- 2- top3 products at each territory for 2013
/*productid             territory
production.product     sales.salesterritory
where year(orderdate)=2013 */

select top(3) p.productid ,count( st.territoryid) territory
from production.product p join sales.SalesOrderDetail so 
on p.ProductID=so.ProductID
join sales.SalesOrderHeader sor 
on so.SalesOrderID=sor.SalesOrderID
join sales.SalesTerritory st 
on st.TerritoryID=sor.TerritoryID
where year(OrderDate)=2013
group by p.productid
order by p.ProductID



-------------------------------------------------------------------------
-- 3- how many employees for each jobtitle

/*employeeid      from               humanresource.employee               
 jobtitle         from               humanresources.employee */
 select jobtitle ,count(*) employees_number
 from  humanresources.employee
 group by jobtitle
 order by count(BusinessEntityID)
-------------------------------------------------------------------------------------
-- 5- list sales persons who sold product called "AWC Logo Cap" how many and how much
/* salespersonid             from person.person or sales.person or sales.salesorderheader   
  sum(productid)              from salesoerderdetails
  where p.name="AWC Logo Cap"  from production.product  */
    
select salespersonid ,count(p.ProductID)
from sales.SalesOrderHeader soh join sales.SalesOrderDetail sod
on soh.SalesOrderID=sod.SalesOrderID
join Production.Product p 
on p.ProductID=sod.ProductID
where p.name = 'AWC Logo Cap'
group by SalesPersonID
order by SalesPersonID