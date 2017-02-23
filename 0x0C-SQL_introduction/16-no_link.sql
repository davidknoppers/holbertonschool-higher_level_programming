-- displays records by score and name, if both exist
-- skips if no name
SELECT `score`, `name`
FROM second_table
WHERE (`name` IS NOT NULL)
ORDER BY `score` DESC;
