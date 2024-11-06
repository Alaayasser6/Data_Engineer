--[main data]
--- How many employee in our company
select count(*)
from HumanResources.Employee    --(290)

---List all department in our country
select Name
from HumanResources.Department;
/* 16 department */

--How many employee in each department

with modifieddate (BusinessEntityID ,modifieddate)
 as (select BusinessEntityID ,max(modifieddate)
from HumanResources.EmployeeDepartmentHistory
group by BusinessEntityID)

select D.name ,count(EDH.BusinessEntityID) NumberofEmployee , dense_rank () over (order by  count(EDH.BusinessEntityID) desc) ranking 
from HumanResources.EmployeeDepartmentHistory EDH
join modifieddate 
on modifieddate.BusinessEntityID = EDH.BusinessEntityID
join HumanResources.Department  D
on D.DepartmentID=EDH.DepartmentID
where modifieddate.modifieddate = EDH.ModifiedDate
group by D.name ;
/*production department is the most department has employee (179)*/

---How many employee in each shift 
with modifieddate (BusinessEntityID ,modifieddate)
 as (select BusinessEntityID ,max(modifieddate)
from HumanResources.EmployeeDepartmentHistory
group by BusinessEntityID)

select sh.Name,count(E.BusinessEntityID) NumberofEmployee 
from  HumanResources.Employee E 
join HumanResources.EmployeeDepartmentHistory EDH
on EDH.BusinessEntityID =E.BusinessEntityID
join modifieddate
on modifieddate.BusinessEntityID =EDH.BusinessEntityID
join HumanResources.Shift sh
on sh.ShiftID= EDH.ShiftID
where modifieddate.modifieddate =EDH.ModifiedDate
group by  sh.name ;
/*  day     176
    evening 62
	night   52  */

                                                                                                                     --[Recruitment KPIS]
---How many employee in each  jobtitle
select JobTitle, count(E.BusinessEntityID) NumberofEmployees 
from  HumanResources.Employee E 
group by  JobTitle
order by count(E.BusinessEntityID)

-----------------------------------------------------------------------------------------
-- job title that has 1 employeee and there organizationlevel
with NumberofEmployee
as(select JobTitle,OrganizationLevel,count(E.BusinessEntityID) NumberofEmployee 
from  HumanResources.Employee E 
group by JobTitle ,OrganizationLevel )

 select * 
from NumberofEmployee
where NumberofEmployee = 1

--count how many job title  has 1 employee in each organization level  
with NumberofEmployee
as(select JobTitle,OrganizationLevel,count(E.BusinessEntityID) NumberofEmployee 
from  HumanResources.Employee E 
group by JobTitle ,OrganizationLevel )

 select OrganizationLevel , count (*)Numberofemployee
from NumberofEmployee
where NumberofEmployee = 1
group by OrganizationLevel;
/* 6 in 1
   13 in 2
   9 in 3
   1 in 4
   1 in null(BOSS)*/
-------------------------------------------------------------------------------------------
--Turnover
 --percentage of employee who still work in our copmany
 with workingemployee (workingemployee)
 as(select count(businessentityid)
 from HumanResources.EmployeeDepartmentHistory
 where EndDate IS NULL) ,
 allemployee (allemployee)
 as (select count (BusinessEntityID)
from HumanResources.Employee)

select workingemployee.workingemployee /allemployee.allemployee*100
from workingemployee,allemployee;
--percentage is 100% so no employee leave the company 
--this is good 
--there is no employee leaves the company in the first date 
----------------------------------------------------------------------------------------------
--the last date we hired new employee
select Max(E.HireDate)
from HumanResources.Employee E ;
--this is old date so need to hire new employee
-----------------------------------------------------------------------------------------------

--job candicate acceptance rate
select count (BusinessEntityID)
from HumanResources.JobCandidate
where BusinessEntityID is not null
/* there is  only two candicates of job were hired 
 أسباب عدم تعين الأخرين إن اتعرض عليهم من منافسين أخرين بمرتبات أعلى  أو التأخر في الرد*/  
----------------------------------------------------------------------------------------------------------------------------------------------------------
/* missing data for hiring cost 
   the sources you hire from it  or advertise */

----------------------------------------------------------------------------------------------------------------------------------------------------------
--[Employee Engagment KPIS]
-- How many employee change their position
with sub (businessID,count)
as(select BusinessEntityID , count(BusinessEntityID)
from HumanResources.EmployeeDepartmentHistory 
group by BusinessEntityID
having count (BusinessentityID) != 1)
	select count (businessID)
	from sub 
--there is 5 employee change their Department
--this is not effective percentage 
-----------------------------------------------------------------------
select EDH.BusinessEntityID ,EDH.DepartmentID ,D.Name, JobTitle
from HumanResources.EmployeeDepartmentHistory EDH join HumanResources.Employee E
ON EDH.BusinessEntityID = E.BusinessEntityID
join HumanResources.Department D
on D.DepartmentID=EDH.DepartmentID
where EDH.BusinessEntityID in (4,16,224,234,250)
--they change department but not job title
-----------------------------------------------------------------------
--Name of these employee ,their city and state ,changenumber
select EDH.BusinessEntityID ,FirstName ,A.City, Name , (count(EDH.BusinessEntityID) -1) changingnumber
from HumanResources.EmployeeDepartmentHistory EDH join person.Person p
on EDH.BusinessEntityID=p.BusinessEntityID
join Person.BusinessEntityAddress  BEA
on BEA.BusinessEntityID=p.BusinessEntityID
join Person.Address A 
on A.AddressID=BEA.AddressID
join person.StateProvince SP 
on sp.StateProvinceID = A.StateProvinceID
group by EDH.BusinessEntityID ,FirstName ,p.Title,A.City ,Name
having count (EDH.BusinessEntityID) != 1

---most of them from washington 
--this is not dirrect relation to hire from this state but may be help
------------------------------------------------------------------------------------------------------
-- how many year between changing 
with progress (BusinessEntityID,FirstName,yearsbetweenchange)
as (select EDH.BusinessEntityID , p.FirstName ,
datediff(year, lag (startdate ,1 ) over (partition by  EDH.BusinessEntityID order by EDH.BusinessEntityID) , startdate) progress
from HumanResources.EmployeeDepartmentHistory EDH join Person.Person p
on EDH.BusinessEntityID = p.BusinessEntityID
where EDH.BusinessEntityID in (4,16,224,234,250))

select * 
from progress
where yearsbetweenchange is not null

-- the most progressed employee sheela  ( change twice and the period between changing is short )

--last year updating pay
select BusinessEntityID ,max (ratechangedate)lastupdating
from HumanResources.EmployeePayHistory
group by  BusinessEntityID ;

--average salary
with last_updating  (BusinessEntityID ,max )
as(select BusinessEntityID ,max (ratechangedate)
from HumanResources.EmployeePayHistory
group by  BusinessEntityID  )

select avg(rate * PayFrequency ) avg
from  HumanResources.EmployeePayHistory EPH  join   last_updating lp
on lp.BusinessEntityID = EPH.BusinessEntityID
where lp.max= EPH.RateChangeDate

--this is low salary 

--top salary
with last_updating  (BusinessEntityID ,max )
as(select BusinessEntityID ,max (ratechangedate)
from HumanResources.EmployeePayHistory
group by  BusinessEntityID  )

select lp.BusinessEntityID,concat(FirstName,' ',LastName),(rate * PayFrequency) ratefreq ,rank () over (order by rate * PayFrequency desc) rank
from  HumanResources.EmployeePayHistory EPH  left join   last_updating lp
on lp.BusinessEntityID = EPH.BusinessEntityID
join Person.Person p
on p.BusinessEntityID= lp.BusinessEntityID
where  lp.BusinessEntityID =  EPH.BusinessEntityID and lp.max= EPH.RateChangeDate

/* top salary (251) ken sanchez (BOSS of Company)*/

----------------------------------------------------------------
with sub (businessID,count)
as(select BusinessEntityID , count(BusinessEntityID)
from HumanResources.EmployeePayHistory 
group by BusinessEntityID
having count (BusinessentityID) != 1)
	select count (businessID)
	from sub ;

--13 employee proggresed their salary 
--so the company must take training

-- to make your next budget this may help you
-- total employee salaries
with last_updating  (BusinessEntityID ,max )
as(select BusinessEntityID ,max (ratechangedate)
from HumanResources.EmployeePayHistory
group by  BusinessEntityID  )

select sum(rate * PayFrequency ) 
from  HumanResources.EmployeePayHistory EPH  left join   last_updating lp
on lp.BusinessEntityID = EPH.BusinessEntityID
where  lp.BusinessEntityID =  EPH.BusinessEntityID and lp.max= EPH.RateChangeDate








