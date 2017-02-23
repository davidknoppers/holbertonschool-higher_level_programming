-- displays averages from a downloaded table dump
-- in descending order
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
