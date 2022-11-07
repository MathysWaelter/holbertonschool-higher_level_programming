-- lists all the cities that can be found in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities
JOIN states on cities.state_id
ORDER BY state_id;