/*
Find students whose CGPA is above the overall average CGPA.
*/
SELECT name
FROM students
WHERE cgpa > (
    SELECT AVG(cgpa)
    FROM students
    );

/*
Find the student(s) with the highest CGPA.
*/
SELECT name
FROM students
where cgpa IN (
    SELECT MAX(cgpa)
    FROM students
    );

/*
Using the marks table, find students who scored more than 90 in any subject.
Return: name
*/

SELECT name
FROM students
where id > (
    SELECT student_id
    FROM marks
    WHERE score > 90
    );

/*
Find students who do not appear in the marks table.
Return:name
*/
SELECT name
FROM students
WHERE id NOT IN (
    SELECT student_id
    FROM marks
    );

/*
Find students whose average marks are greater than the overall average marks.
Expected columns:
name
average_score
Hint:
You'll need:
GROUP BY
and a subquery containing:
AVG()
*/
SELECT
    s.name,
    AVG(m.score) AS average_score
FROM students AS s
JOIN marks AS m
    ON s.id = m.student_id
GROUP BY s.id, s.name
HAVING AVG(m.score) > (
    SELECT AVG(score)
    FROM marks
);

/*
Suppose:
students
id | name | cgpa
and:
marks
student_id | subject | score
A student can have multiple marks.
Why might this query produce duplicate names?

SELECT s.name
FROM students AS s
JOIN marks AS m
    ON s.id = m.student_id
WHERE m.score > 80;

How could you remove the duplicates?

GROUP BY isn't required to avoid duplicates—DISTINCT is the simplest solution here.
SELECT DISTINCT s.name
FROM students AS s
JOIN marks AS m
    ON s.id = m.student_id
WHERE m.score > 80;
*/

/*
# SQL — Lesson 6: Subqueries

## What is a Subquery?

A subquery is a **query inside another query**.

It is used to break a complex problem into smaller queries and use the result of one query in another.

Example:

```sql
SELECT name
FROM students
WHERE cgpa > (
    SELECT AVG(cgpa)
    FROM students
);
```

The inner query calculates the average CGPA, and the outer query finds students above that average.

---

## Why use Subqueries?

* Solve complex queries step-by-step
* Use the result of one query in another
* Compare values with aggregate results
* Filter data using another query
* Useful in SQL interviews and OAs

---

## Single-Value Subquery

A subquery that returns one value can be used with:

```sql
=
>
<
>=
<=
```

Example:

```sql
SELECT name, cgpa
FROM students
WHERE cgpa = (
    SELECT MAX(cgpa)
    FROM students
);
```

`MAX()` returns one value, so `=` can be used.

---

## Multi-Value Subquery

When a subquery can return multiple values, use `IN`.

```sql
SELECT name
FROM students
WHERE id IN (
    SELECT student_id
    FROM marks
    WHERE score > 90
);
```

The inner query can return multiple `student_id` values.

---

## `IN`

Checks whether a value exists in the results of a subquery.

```sql
SELECT name
FROM students
WHERE id IN (
    SELECT student_id
    FROM marks
);
```

---

## `NOT IN`

Find values that do not exist in the subquery result.

```sql
SELECT name
FROM students
WHERE id NOT IN (
    SELECT student_id
    FROM marks
);
```

This can find students who have no records in `marks`.

---

## Subquery with Aggregate Functions

### Above average

```sql
SELECT name, cgpa
FROM students
WHERE cgpa > (
    SELECT AVG(cgpa)
    FROM students
);
```

### Highest CGPA

```sql
SELECT name, cgpa
FROM students
WHERE cgpa = (
    SELECT MAX(cgpa)
    FROM students
);
```

### Lowest CGPA

```sql
SELECT name, cgpa
FROM students
WHERE cgpa = (
    SELECT MIN(cgpa)
    FROM students
);
```

---

## Subquery vs JOIN

### Subquery

Used when the result of one query is needed to filter another query.

```sql
SELECT name
FROM students
WHERE id IN (
    SELECT student_id
    FROM marks
    WHERE score > 90
);
```

### JOIN

Used to combine related rows from multiple tables.

```sql
SELECT DISTINCT s.name
FROM students AS s
JOIN marks AS m
    ON s.id = m.student_id
WHERE m.score > 90;
```

Both can sometimes solve the same problem.

---

## Correlated Subquery

A correlated subquery depends on the **current row of the outer query**.

Example:

```sql
SELECT s.name, s.cgpa
FROM students AS s
WHERE s.cgpa > (
    SELECT AVG(s2.cgpa)
    FROM students AS s2
    WHERE s2.branch = s.branch
);
```

This finds students whose CGPA is higher than the average CGPA of their own branch.

Important:

```text
Normal subquery
→ Independent of outer query

Correlated subquery
→ Depends on outer query row
```

---

## Important Interview Questions

**1. What is a subquery?**

A query written inside another query, used to solve complex queries by using the result of one query in another.

**2. Why are subqueries useful?**

They make complex queries easier to divide, understand, and solve.

**3. Difference between `=` and `IN` with subqueries?**

`=` is used when comparing against a single value, while `IN` is used when the subquery can return multiple values.

**4. Can a subquery return multiple rows?**

Yes.

**5. Can a subquery return multiple columns?**

Yes, depending on how the subquery is used.

**6. Difference between JOIN and subquery?**

JOIN combines related data from tables, while a subquery uses the result of one query inside another query.

**7. What is a correlated subquery?**

A subquery that depends on values from the current row of the outer query.

**8. Can a query using `MAX()` return multiple rows?**

Yes. If multiple records have the same maximum value, all matching records can be returned.

---

## Key Things to Remember

```text
Subquery
→ Query inside another query

=
→ Single-value comparison

IN
→ Multiple-value comparison

NOT IN
→ Values absent from subquery result

Subquery + AVG()
→ Compare against average

Subquery + MAX()
→ Find highest value

Subquery + MIN()
→ Find lowest value

Correlated subquery
→ Inner query depends on outer query

JOIN
→ Combines related tables

Subquery
→ Uses result of one query inside another
```
*/

