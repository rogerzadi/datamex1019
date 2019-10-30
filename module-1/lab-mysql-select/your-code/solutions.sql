## Challenge1
SELECT au.au_id as AUTHOR_ID, au.au_lname as LAST_NAME, au.au_fname as FIRST_NAME, t.title as TITLE, 
pu.pub_name as PUBLISHERS
from 
authors as au
left join titleauthor as ti
on au.au_id = ti.au_id
inner join titles t
on ti.title_id=t.title_id
inner join publishers pu
on t.pub_id= pu.pub_id

##Challenge2

select AUTHOR_ID, LAST_NAME, FIRST_NAME, PUBLISHERS, count(title) as Count_Titles from(
SELECT au.au_id as AUTHOR_ID, au.au_lname as LAST_NAME, au.au_fname as FIRST_NAME, t.title as TITLE, 
pu.pub_name as PUBLISHERS
from 
authors as au
left join titleauthor as ti
on au.au_id = ti.au_id
inner join titles t
on ti.title_id=t.title_id
inner join publishers pu
on t.pub_id= pu.pub_id) Resu
group by AUTHOR_ID, PUBLISHERS

##Challenge3
select au.au_id as AUTHORID, au.au_lname as LASTNAME, au.au_fname as FIRSTNAME, sum(sal.qty) as TOTAL
from authors au
inner join titleauthor as tau
on au.au_id = tau.au_id
inner join sales as sal
on tau.title_id = sal.title_id
group by AUTHORID
order by TOTAL desc
limit 3 ;

##Challenge 4
select au.au_id as AUTHORID, au.au_lname as LASTNAME, au.au_fname as FIRSTNAME, COALESCE(sum(sal.qty),0) as TOTAL
from authors au
left join titleauthor as tau
on au.au_id = tau.au_id
left join sales as sal
on tau.title_id = sal.title_id
group by AUTHORID
order by TOTAL desc
;