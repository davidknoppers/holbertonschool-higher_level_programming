-- displays the max temp recorded for each state
-- no clear ordering
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state;
