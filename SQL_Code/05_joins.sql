PRAGMA table_info(marks);
SELECT * FROM marks;

SELECT
    s.name,
    s.branch,
    m.subject,
    m.score
FROM students AS s
JOIN marks AS m
    ON s.id = m.student_id;

INSERT INTO marks (student_id, subject, score)
VALUES
    (1, 'Python', 85),
    (1, 'SQL', 78),
    (2, 'Python', 92),
    (2, 'SQL', 88),
    (3, 'Python', 76),
    (3, 'SQL', 81),
    (4, 'Python', 69),
    (5, 'Python', 95),
    (5, 'SQL', 91);

PRAGMA table_info(marks);
SELECT * FROM marks;

DELETE FROM marks;

INSERT INTO marks (student_id, subject, score)
VALUES
    (1, 'Python', 85),
    (1, 'SQL', 78),
    (2, 'Python', 92),
    (2, 'SQL', 88),
    (3, 'Python', 76),
    (3, 'SQL', 81),
    (4, 'Python', 69),
    (5, 'Python', 95),
    (5, 'SQL', 91);

SELECT * FROM marks;

SELECT
    s.name,
    s.branch,
    m.subject,
    m.score
FROM students AS s
JOIN marks AS m
    ON s.id = m.student_id;

SELECT
    s.name,
    s.branch,
    m.subject,
    m.score
FROM students AS s
LEFT JOIN marks AS m
    ON s.id = m.student_id;

SELECT
    s.name
FROM students AS s
LEFT JOIN marks AS m
    ON s.id = m.student_id
WHERE m.student_id IS NULL;

SELECT
    s.name,
    m.subject,
    m.score
FROM students AS s
JOIN marks AS m
    ON s.id = m.student_id
WHERE m.score > 80;

SELECT
    s.name,
    m.subject,
    m.score
FROM students AS s
JOIN marks AS m
    ON s.id = m.student_id
ORDER BY m.score DESC;

SELECT
    s.name,
    AVG(m.score) AS average_score
FROM students AS s
JOIN marks AS m
    ON s.id = m.student_id
GROUP BY s.id, s.name;

SELECT
    s.branch,
    AVG(m.score) AS average_score
FROM students AS s
JOIN marks AS m
    ON s.id = m.student_id
GROUP BY s.branch;

SELECT
    s.branch,
    AVG(m.score) AS average_score
FROM students AS s
JOIN marks AS m
    ON s.id = m.student_id
GROUP BY s.branch
HAVING AVG(m.score) > 80;

/*
Return:
student name
subject
score
for every student who scored at least 80.
*/

SELECT 
    s.name,
    m.subject,
    m.score
FROM students AS s
JOIN marks AS m
    ON s.id = m.student_id
WHERE m.score > 80;

/*
Return every student and their marks.
Students without marks must also appear.
*/
SELECT
    s.name,
    m.subject,
    m.score
FROM students AS s
LEFT JOIN marks as m
    ON s.id = m.student_id;

/*
Find the average score of each student.
Expected columns:
name | average_score
*/
SELECT
    s.name,
    AVG(m.score) AS avg_score
FROM students AS s
LEFT JOIN marks AS m 
    ON s.id = m.student_id
GROUP BY s.name;

/*
Find the highest score obtained by each student.
*/

SELECT
    s.name,
    MAX(m.score) as highest_score
FROM students as s
LEFT JOIN marks as m 
    on s.id = m.student_id
GROUP BY s.id, s.name;

/*
Find the average score for each branch and sort from 
highest average to lowest.
*/
SELECT
    s.branch,
    AVG(m.score) as average_score
FROM students as s
LEFT JOIN marks as m
    ON s.id = m.student_id
GROUP BY s.branch
ORDER BY AVG(m.score) DESC;

/*
Find the students whose average score is greater than 80.
*/
SELECT
    s.name,
    AVG(score) as average_score
FROM students as s
LEFT JOIN marks as m
    ON s.id = m.student_id
GROUP BY s.name
HAVING AVG(m.score) > 80;

/*
Find students who have no marks at all.
*/
SELECT
    s.name
FROM students AS s
LEFT JOIN marks AS m
    ON s.id = m.student_id
WHERE m.student_id IS NULL;