-- displays a count of each score
-- in descending order
SELECT `score`, COUNT(`score`) as number
FROM second_table
GROUP BY `score`
ORDER BY number DESC;
