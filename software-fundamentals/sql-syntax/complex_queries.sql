-- Using the Pokemon database, write a query that returns the average weight for each primary type.

SELECT t.type_name, ROUND(AVG(p.pokemon_weight), 2) AS average_weight
FROM pokemon AS p
JOIN type_assignment AS ta USING(pokemon_id)
JOIN pokemon_type as t USING(type_id)
GROUP BY t.type_name
ORDER BY average_weight DESC
LIMIT 20;

-- Subqueries
-- A query that returns the pokemon name and types for pokemon greater than the average weight and height

SELECT p.pokemon_name, STRING_AGG(t.type_name, ', ') as types, p.pokemon_weight
FROM pokemon AS p
JOIN type_assignment AS ta USING(pokemon_id)
JOIN pokemon_type as t USING(type_id)
WHERE p.pokemon_height > (
    SELECT avg(pokemon_height) as average_height
    FROM pokemon
) AND p.pokemon_weight > (
    SELECT avg(pokemon_weight) as average_weight
    FROM pokemon
)
GROUP BY p.pokemon_name, p.pokemon_weight
LIMIT 10;

-- Common Table Expressions (CTEs)
WITH 
    avg_weight AS (
        SELECT avg(pokemon_weight) as average_weight, COUNT(*) as COUNT
        FROM pokemon
    ),
    avg_height AS (
        SELECT avg(pokemon_height) as average_height
        FROM pokemon
    )
SELECT p.pokemon_name, STRING_AGG(t.type_name, ', ') AS types, p.pokemon_weight
FROM pokemon as p
JOIN type_assignment as ta USING(pokemon_id)
JOIN pokemon_type as t USING(type_id)
WHERE p.pokemon_weight > (SELECT average_weight FROM avg_weight)
    AND p.pokemon_height > (SELECT * FROM avg_height)
GROUP BY p.pokemon_name, p.pokemon_weight
LIMIT 10;

-- Write a query that finds the name and types of each pokemon that has more than one type
WITH 
    type_count AS (
        SELECT ta.pokemon_id, COUNT(ta.pokemon_id) AS count FROM pokemon
        JOIN type_assignment as ta USING(pokemon_id)
        JOIN pokemon_type as t USING(type_id)
        GROUP BY ta.pokemon_id
    )

SELECT p.pokemon_name, STRING_AGG(t.type_name, ', ') AS types
FROM pokemon as p
JOIN type_assignment as ta USING(pokemon_id)
JOIN pokemon_type as t USING(type_id)
JOIN type_count USING (pokemon_id)
WHERE type_count.count > 1
GROUP BY p.pokemon_name
;


WITH 
    multitypes AS (
        SELECT pokemon_id
        FROM type_assignment
        GROUP BY pokemon_id
        HAVING COUNT(*) > 1
    )
SELECT p.pokemon_name, STRING_AGG(t.type_name, ', ') AS types
FROM pokemon as p
JOIN type_assignment as ta USING(pokemon_id)
JOIN pokemon_type as t USING(type_id)
WHERE p.pokemon_id IN (
    select pokemon_id FROM multitypes
)
GROUP BY p.pokemon_id, p.pokemon_name
LIMIT 10;

SELECT * FROM pokemon;

SELECT pokemon_name, pokemon_id FROM pokemon;

SELECT pokemon_name, pokemon_id 
FROM pokemon
WHERE pokemon_name ILIKE '%SAUR%';


SELECT pokemon_name, pokemon_id, p.pokemon_weight
FROM pokemon
WHERE pokemon_name ILIKE '%SAUR%'
GROUP BY pokemon_id;

-- The average height of fire-type Pokemon compared to water-type Pokemon


-- The secondary type with the lowest maximum weight


-- The name of the primary type with the longest average description length
