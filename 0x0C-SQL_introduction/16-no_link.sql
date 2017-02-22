-- displays records by score and name, if both exist
SELECT `score`, `name`
FROM second_table
WHERE (`name` IS NOT NULL)
ORDER BY `score` DESC;
