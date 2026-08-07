SELECT *
FROM students;

SELECT *
FROM students;

SELECT *
FROM students
WHERE branch = 'IT';

SELECT *
FROM students
WHERE age >21;

SELECT *
FROM students
WHERE cgpa >= 7.5;

SELECT *
FROM students
WHERE branch = 'IT'
AND cgpa >= 7.5;
/*
Why isn't OR correct here?
or is used to give either of the two conditions
*/

SELECT *
FROM students
WHERE branch = 'CSE'
OR branch = 'IT';

SELECT *
FROM students
WHERE NOT branch = 'IT';

SELECT *
FROM students
WHERE age BETWEEN 21 AND 22;
/*
Does BETWEEN include both endpoints?
YES
*/

SELECT *
FROM students
WHERE branch IN ('IT', 'CSE');

SELECT *
FROM students
WHERE name LIKE 'R%';

SELECT *
FROM students
WHERE name LIKE '%A';

SELECT *
FROM students
WHERE name LIKE '%AV%';
/*
What does % mean?
% is a wildcard that represents zero or more characters.
*/

--Students younger than 23.
SELECT *
FROM students
WHERE age<23;

--Students with CGPA less than 8.
SELECT *
FROM students
WHERE cgpa <8;

--Students in CSE.
SELECT *
FROM students
WHERE branch = 'CSE';

--IT students aged 22.
SELECT *
FROM students
WHERE branch = 'IT'
AND age = 22;

--CSE students with CGPA above 7.
SELECT *
FROM students
WHERE branch = 'CSE'
AND cgpa > 7;

--BETWEEN
SELECT *
FROM students
WHERE age BETWEEN 21 AND 22;

--IN
SELECT *
FROM students
WHERE branch IN ('IT');

--NOT
SELECT *
FROM students
WHERE NOT branch = 'IT';

--Names starting with P.
SELECT *
FROM students
WHERE name LIKE 'P%';

--Names containing a.
SELECT *
FROM students
WHERE name LIKE '%A%';

--Names ending with i.
SELECT *
FROM students
WHERE NAME LIKE '%I';

/*
What does WHERE do?
where is used as a filter apply a condition

Difference between WHERE and HAVING? (We'll study HAVING later—just note that it's related to grouped data.)
WHERE filters rows before grouping. HAVING filters groups after GROUP BY.

Difference between = and LIKE.
= checks for an exact match, whereas LIKE matches patterns using wildcards such as % and _.

What does % mean in SQL?
% is a wildcard that represents zero or more characters.

Why is IN better than multiple OR conditions?
in provides better scalability for multiple conditions
*/

/*
Without running the query, predict the output:

SELECT name
FROM students
WHERE age BETWEEN 21 AND 22
AND branch = 'IT';

Which names will be returned?Explain why.

raj beacuse it is between the age of 21 and 22 and the branch is IT.
*/
