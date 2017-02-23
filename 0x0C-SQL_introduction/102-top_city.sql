-- displays top 3 cities by temp
-- in July and August
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month IN (7, 8)
GROUP BY city ORDER BY avg_temp desc LIMIT 3;
