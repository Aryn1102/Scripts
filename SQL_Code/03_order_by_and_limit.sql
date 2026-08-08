SELECT *
FROM students
ORDER BY cgpa;
/*
Predict the order before running.
raj, ravi, aman, priya
*/

SELECT *
FROM students
ORDER BY cgpa DESC;
/*
Who appears first?
priya
*/

SELECT *
FROM students
ORDER BY cgpa ASC;

/*
Why are these two identical?
ORDER BY cgpa;
ORDER BY cgpa ASC;
asc is set by default
*/

SELECT *
FROM students
ORDER BY name;

SELECT *
FROM students
ORDER BY name DESC;

SELECT *
FROM students
ORDER BY age,
         cgpa;
/*
Which column has higher priority?
the one which is written first
*/

SELECT *
FROM students
ORDER BY age ASC,
         cgpa DESC;

SELECT *
FROM students
LIMIT 2;

SELECT *
FROM students
ORDER BY cgpa DESC
LIMIT 1;
--Why doesn't this work?
/*SELECT *
FROM students
LIMIT 1
ORDER BY cgpa DESC;*/
--it is a syntax error as order should always come before limit

SELECT name, cgpa
FROM students
WHERE branch = 'IT'
ORDER BY cgpa DESC
LIMIT 1;

--Age ASC
SELECT *
FROM students
ORDER BY age;

--Age DESC
SELECT *
FROM students
ORDER BY age DESC;

--CGPA ASC
SELECT *
FROM students
ORDER BY cgpa;

--CGPA DESC
SELECT *
FROM students
ORDER BY cgpa DESC;

--Name ASC
SELECT *
FROM students
ORDER BY NAME;

--Name DESC
SELECT *
FROM students
ORDER BY NAME DESC;

--Top 2 CGPA students.
SELECT *
FROM students
ORDER BY cgpa DESC
LIMIT 2;

--Youngest student.
SELECT *
FROM students
ORDER BY age 
LIMIT 1;

--Oldest student.
SELECT *
FROM students
ORDER BY age DESC
LIMIT 1;

--Branch then Age.
SELECT *
FROM students
ORDER BY branch,
         age;
--Branch then CGPA DESC.
SELECT *
FROM students
ORDER BY branch,
         CGPA DESC;

--Highest CGPA CSE student.
SELECT *
FROM students
WHERE branch = 'CSE'
ORDER BY CGPA DESC
LIMIT 1;

--Highest CGPA IT student.
SELECT *
FROM students
WHERE branch = 'IT'
ORDER BY CGPA DESC
LIMIT 1;

--The oldest IT student.
SELECT *
FROM students
WHERE branch = 'IT'
ORDER BY age DESC
LIMIT 1;

/*
What does ORDER BY do?
order by sorts the values in ascending order by default and descending if mentioned

Difference between ASC and DESC.
asc arranges values starting from smallest to largest and vice versa for desc

Why is ASC optional?
because asc is default for order by

Difference between WHERE and ORDER BY.
where is a filter used to put a conditon and order by is used to sort the rows

Why is LIMIT useful?
limit is used to put a maximum limit on the no of records
*/

/*
Which column is sorted first?
branch
Why?
because it is mentioned first
Which row appears first?
ravi, because his branch is cse, age highest in cse and he is the only one left after applying those two filters

*/
SELECT *
FROM students
ORDER BY branch,
         age DESC,
         cgpa ASC;

/*
If two students have exactly the same CGPA, is SQL guaranteed to return them in the same order every time?
No.Unless you explicitly tell SQL how to break ties.
*/

SELECT *
FROM students
ORDER BY cgpa DESC
LIMIT 2;