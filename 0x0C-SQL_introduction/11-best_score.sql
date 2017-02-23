-- list all scores of a table
-- that are ten or better
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score desc;
