-- selects cities of California from states in ascending order
SELECT id, name FROM cities
WHERE state_id IN
      (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
