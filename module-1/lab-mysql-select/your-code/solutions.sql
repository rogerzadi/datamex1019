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

SELECT AUTHOR_ID, LAST_NAME, FIRST_NAME, COUNT(TITLE) as TITLE_COUNT
FROM
(SELECT a.au_id as AUTHOR_ID, a.au_lname as LAST_NAME, a.au_fname as FIRST_NAME, t.title as TITLE
FROM authors as a
left join titleauthor as ta
on ta.au_id= a.au_id
inner join titles t
on ta.title_id = t.title_id
inner join sales s
on t.title_id = s.title_id) as t
GROUP BY AUTHOR_ID
order by TITLE_COUNT desc
limit 3 
;

##Challenge 4

SELECT AUTHOR_ID, LAST_NAME, FIRST_NAME, COUNT(TITLE) as TITLE_COUNT
FROM
(SELECT a.au_id as AUTHOR_ID, a.au_lname as LAST_NAME, a.au_fname as FIRST_NAME, t.title as TITLE
FROM authors as a
left join titleauthor as ta
on ta.au_id= a.au_id
left join titles t
on ta.title_id = t.title_id
left join sales s
on t.title_id = s.title_id) as t
GROUP BY AUTHOR_ID
order by TITLE_COUNT asc
;