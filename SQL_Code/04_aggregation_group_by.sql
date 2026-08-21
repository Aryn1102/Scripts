SELECT COUNT(*)
FROM students;

SELECT AVG(cgpa)
FROM students;

SELECT MAX(cgpa)
FROM students;

SELECT MIN(cgpa)
FROM students;

SELECT SUM(age)
FROM students;

/*
COUNT(*) vs COUNT(column)

SELECT COUNT(*)
FROM students;
counts rows.

SELECT COUNT(cgpa)
FROM students;
counts non-NULL CGPA values.
*/

SELECT branch, AVG(cgpa)
FROM students
GROUP BY branch;

SELECT branch, COUNT(*)
FROM students
GROUP BY branch;

SELECT
    branch,
    COUNT(*) AS student_count,
    AVG(cgpa) AS average_cgpa,
    MAX(cgpa) AS highest_cgpa,
    MIN(cgpa) AS lowest_cgpa
FROM students
GROUP BY branch;

SELECT branch, AVG(cgpa)
FROM students
WHERE cgpa >= 7
GROUP BY branch;

SELECT branch, AVG(cgpa)
FROM students
GROUP BY branch
HAVING AVG(cgpa) > 7.5;

SELECT branch, AVG(cgpa)
FROM students
WHERE age >= 21
GROUP BY branch
HAVING AVG(cgpa) > 7;

SELECT branch, age, COUNT(*)
FROM students
GROUP BY branch, age;

/*
SQL Execution order
FROM
 ↓
WHERE
 ↓
GROUP BY
 ↓
HAVING
 ↓
SELECT
 ↓
ORDER BY
 ↓
LIMIT
*/

/*
Interview Questions
Answer these yourself before looking anything up.
Q1 What does COUNT(*) do?
counts rows
Q2 What's the difference between:
COUNT(*) and COUNT(cgpa)?
* counts rows and cgpa counts non null rows of cgpa

Q3 What is the purpose of GROUP BY?
GROUP BY divides rows into groups based on one or more columns so aggregate functions can calculate statistics for each group.

Q4 What's the difference between WHERE and HAVING?
where is used to filter on all rows and having filters after aggregation

Q5 Why can't we normally write:
WHERE AVG(cgpa) > 7?
aggregation applies after grouping not directly on all rows

Q6 What does AS do?
AS creates an alias (temporary output name) for a column or expression.

Q7 Can you group by multiple columns?
yes
*/

--Find the total number of students.
SELECT count(*)
FROM students;

--Find the average CGPA.
SELECT avg(cgpa)
FROM students;

--Find the highest CGPA.
SELECT max(cgpa)
FROM students;

--Find the number of students in each branch.
SELECT branch, count(*)
FROM students
GROUP BY branch;

--Find the average CGPA for each branch.
SELECT branch, avg(cgpa)
FROM students
GROUP BY branch;

--Find branches having more than 2 students.
SELECT branch, count(*)
FROM students
GROUP BY branch
HAVING count(*) >= 2;

--Find the branch with the highest average CGPA.
SELECT branch, avg(cgpa)
FROM students
GROUP BY branch
ORDER BY avg(cgpa) DESC
LIMIT 1;
